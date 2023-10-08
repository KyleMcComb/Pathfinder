# below imports are used for sending an email
import base64
import qrcode
import smtplib
import io
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from database.models import *
from mysite.settings import *
from django.http import JsonResponse
from django.http import HttpResponse
from main.forms import CustomLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django_otp.plugins.otp_totp.models import TOTPDevice

'''
    @Author: @DeanLogan
    @Description: Gets the username and password from the request then checks if these credentials are on the system, returns true or false based on authentication result.
    @param: request -  HttpRequest object that contains metadata about the request
    @return: loggedIn - JSON object containing whether or not a the log in attempt was successful
'''
def verify(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        # Check if form is valid, if it is not valid then the user has failed the captcha
        if form.is_valid():
            authenticatedUser = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if hasTwoFactorEnabled(authenticatedUser):
                if verifyTotpCode(authenticatedUser, request) == False:
                    return JsonResponse({'loggedIn': 'false', 'errors': 'Failed 2FA, wrong code'})
            login(request, authenticatedUser)
            # Set session timeout based on 'remember_me' value
            if form.cleaned_data.get('remember_me', False):
                request.session.set_expiry(1209600)  # Two weeks (in seconds)
            return JsonResponse({'loggedIn': 'true'})
        else:
            return JsonResponse({'loggedIn': 'false', 'errors': 'Failed Captcha, or invalid credentials'})
    else:
        return JsonResponse({'errors': 'Invalid request method'})

# the below function will be used to check if the user has 2FA enabled, for now it will return True just for testing purposes
def hasTwoFactorEnabled(authenticatedUser):
    try:
        totp_device = TOTPDevice.objects.filter(user=authenticatedUser)
        for device in totp_device:
            if device.confirmed:
                return True
    except TOTPDevice.DoesNotExist:
        pass
    return False

def verifyTotpCode(authenticatedUser, request):
    try:
        totp_device = TOTPDevice.objects.filter(user=authenticatedUser)
        for device in totp_device:
            if device.verify_token(request.POST['code']):
                return True
    except TOTPDevice.DoesNotExist:
        # Handle the case where the user doesn't have a TOTP device
        pass
    return False

def createSecretKey(request):
    return TOTPDevice.objects.create(user=request.user, confirmed=True).config_url

def generateQRCode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer)
    buffer.seek(0)
    base64_image = base64.b64encode(buffer.read()).decode("utf-8")

    return base64_image  # Return the Base64-encoded image data

def displayQRCode(request):
    return HttpResponse(generateQRCode(createSecretKey(request)), content_type="image/png")

'''
    @Author: @DeanLogan
    @Description: Gets the information needed for sign-up then sends an email containing this informatuion, or if email cannot be sent a fail message. 
    @param: request -  HttpRequest object that contains metadata about the request
    @return: success - JSON object containing true or false (stored as string as in Django a response can only have a JSON object with strings), depending if a successful email was sent to the admin
'''
def signUp(request):
    # get required info
    success = {'success':'true'}
    try:
        studentNumber = request.GET.get('studentNumber')
        name = request.GET.get('name')
        email = request.GET.get('email')
        selectedPathway = request.GET.get('selectedPathway')
        currentStage = request.GET.get('currentStage')
        currentSemester = request.GET.get('currentSemester')

        admin = User.objects.get(username='admin')
        adminEmail = admin.email

        # below formats the information into an email
        msg = MIMEMultipart()
        msg['From'] = 'pathfinder3068@gmail.com'
        msg['To'] = "{0}".format(adminEmail)
        msg['Subject'] = 'Sign-Up User'

        messageContentInHtml = '<h1>Request has been made to sign up user</h1><br/><p><b>Student Number: </b>'+studentNumber+'</p><p><b>Name: </b>'+name+'</p><p><b>Email: </b>'+email+'</p><p><b>Pathway: </b>'+selectedPathway+'</p><p><b>Stage: </b>'+currentStage+'</p><p><b>Semester: </b>'+currentSemester+'</p><br/><p>From Pathfinder.'

        body = MIMEText(messageContentInHtml, 'html')
        msg.attach(body)

        server = smtplib.SMTP('smtp.gmail.com', 587) # connect to email server
        server.starttls() #encrypts login
        server.login('pathfinder3068@gmail.com', 'eglrgyaxlnyrvixi') # email account and 3rd party app password for the account which the email will be sent from
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        success = {'success':'false'}

    return JsonResponse(success, safe=False)

