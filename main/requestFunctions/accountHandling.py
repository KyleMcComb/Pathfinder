# below imports are used for sending an email
import io
import json
import base64
import qrcode
import smtplib
import re
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

"""
    @Author: @DeanLogan
    @Description: Verifies user authentication, including two-factor authentication (2FA) if enabled.
    @param: request - The HttpRequest object containing user authentication and 2FA information.
    @return: JsonResponse indicating whether the user is logged in ('true' or 'false') and any errors.
"""
def verify(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        
        # Check if the form is valid; if not, the user may have failed the captcha
        if form.is_valid():
            # Attempt to authenticate the user using provided username and password
            authenticatedUser = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
            # Check if 2FA is enabled for the user and verify the TOTP code if necessary
            if json.loads(hasTwoFactorEnabled(request).content.decode('utf-8'))['hasTwoFactorEnabled'] == 'true' and verifyTotpCode(authenticatedUser, request) is False:
                return JsonResponse({'loggedIn': 'false', 'errors': 'Failed 2FA, wrong code'})
            
            # Log in the user if authentication is successful
            login(request, authenticatedUser)
            
            # Set session timeout based on 'remember_me' value
            if form.cleaned_data.get('remember_me', False):
                request.session.set_expiry(1209600)  # Two weeks (in seconds)
            
            return JsonResponse({'loggedIn': 'true'})  # User is successfully logged in
        
        else:
            return JsonResponse({'loggedIn': 'false', 'errors': 'Failed Captcha, or invalid credentials'})  # Captcha or credentials validation failed
    
    else:
        return JsonResponse({'errors': 'Invalid request method'})  # Invalid request method (not POST)

"""
    @Author: @DeanLogan
    @Description: Checks if a user has two-factor authentication (TOTP) enabled.
    @param: request - The HttpRequest object containing the user's authentication information.
    @return: JsonResponse indicating whether two-factor authentication is enabled ('true' or 'false').
"""
def hasTwoFactorEnabled(request):
    if request.method == 'POST':
        try:
            # Attempt to authenticate the user with provided username and password
            form = CustomLoginForm(request, data=request.POST)
            authenticatedUser = authenticate(request, username=form['username'].value(), password=form['password'].value())
            
            # Check if the authenticated user has any TOTP devices and if at least one is confirmed
            totpDevices = TOTPDevice.objects.filter(user=authenticatedUser)
            for device in totpDevices:
                if device.confirmed:
                    return JsonResponse({'hasTwoFactorEnabled': 'true'})  # Two-factor authentication is enabled
        except TOTPDevice.DoesNotExist:
            pass
        
        return JsonResponse({'hasTwoFactorEnabled': 'false'})  # Two-factor authentication is not enabled
        
    else:
        return JsonResponse({'errors': 'Invalid request method'})  # Invalid request method (not POST)

"""
    @Author: @DeanLogan
    @Description: Verifies a TOTP code against the TOTP devices associated with an authenticated user.
    @param: authenticatedUser - The authenticated user whose TOTP devices will be checked.
    @param: request - The HttpRequest object containing the TOTP code to verify.
    @return: True if the TOTP code is valid for any of the user's TOTP devices, False otherwise.
"""
def verifyTotpCode(authenticatedUser, request):
    try:
        totpDevice = TOTPDevice.objects.filter(user=authenticatedUser) # Get all TOTP devices associated with the authenticated user
        for device in totpDevice:
            if device.verify_token(request.POST['code']):
                return True # TOTP code is valid for this device
    except TOTPDevice.DoesNotExist:
        # Handle the case where the user doesn't have a TOTP device
        pass
    return False # TOTP code is not valid for any of the user's TOTP devices

"""
    @Author: @DeanLogan
    @Description: Creates and returns a secret key for two-factor authentication (TOTP).
    @param: request - The HttpRequest object containing metadata about the request.
    @return: The TOTP secret key as a URL for configuration.
"""
def createSecretKey(request):
    return TOTPDevice.objects.create(user=request.user, confirmed=True).config_url

"""
    @Author: @DeanLogan
    @Description: Generates a QR code image from a given URL.
    @param: url - The URL to encode in the QR code.
    @return: Base64-encoded image data of the QR code.
"""
def generateQRCode(url):
    # Create a QR code instance with specified parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the URL data to the QR code
    qr.add_data(url)
    
    # Generate the QR code image and fit it
    qr.make(fit=True)
    
    # Create an image with specified fill and background colors
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Create an in-memory buffer for the image
    buffer = io.BytesIO()
    img.save(buffer)
    
    # Seek to the beginning of the buffer and encode the image in Base64
    buffer.seek(0)
    base64_image = base64.b64encode(buffer.read()).decode("utf-8")

    return base64_image  # Return the Base64-encoded image data

"""
    @Author: @DeanLogan
    @Description: Displays a QR code image containing a secret key.
    @param: request - The HttpRequest object containing metadata about the request.
    @return: HttpResponse containing the QR code image in PNG format.
"""
def displayQRCode(request):
    return HttpResponse(generateQRCode(createSecretKey(request)), content_type="image/png")

"""
    @Author: @DeanLogan
    @Description: Handles the forgot password request. Validates the user's input and sends a password reset request to the admin.
    @param: request - The HttpRequest object containing user input (studentNumber and studentEmail).
    @return: JsonResponse with a status message indicating the result of the password reset request.
"""
def forgotPassword(request):
    try:
        # Get studentNumber and studentEmail from the request
        studentNumber = request.GET.get('studentNumber')
        studentEmail = request.GET.get('studentEmail')
        
        # Replace '%40' with '@' in the studentEmail if necessary
        studentEmail = re.sub('%40', '@', studentEmail)

        # Check if a user with the given username (studentNumber) exists
        if User.objects.filter(username=studentNumber).exists():
            # Check if the provided studentEmail matches the user's email
            if studentEmail == User.objects.get(username=studentNumber).email:
                # Send a password reset request to the admin and return the status
                return JsonResponse({'status': forgotPasswordEmail(studentNumber, studentEmail)}, safe=False)
            else:
                return JsonResponse({'status': 'Wrong Email Entered'}, safe=False)
        else:
            return JsonResponse({'status': 'Username does not exist'}, safe=False)
    except:
        return JsonResponse({'status': 'Error during the request'}, safe=False)

"""
    @Author: @DeanLogan
    @Description: Sends an email to the admin requesting a password reset for a user.
    @param: studentNumber - The student's identification number.
    @param: studentEmail - The student's email address.
    @return: A message indicating whether the email was sent successfully.
"""
def forgotPasswordEmail(studentNumber, studentEmail):
    try:
        admin = User.objects.get(username='admin')
        adminEmail = admin.email

        # below formats the information into an email
        msg = MIMEMultipart()
        msg['From'] = 'pathfinder3068@gmail.com'
        msg['To'] = "{0}".format(adminEmail)
        msg['Subject'] = 'Sign-Up User'

        messageContentInHtml = '<h1>Request has been made to reset password for</h1><br/><p><b>Student Number: </b>'+studentNumber+'</p><p><b>Email: </b>'+studentEmail+'</p><p>Please reset the users password and email them a new one.</p><br/><p>From Pathfinder.'

        body = MIMEText(messageContentInHtml, 'html')
        msg.attach(body)

        server = smtplib.SMTP('smtp.gmail.com', 587) # connect to email server
        server.starttls() # encrypts login
        server.login('pathfinder3068@gmail.com', 'aaiu vmwm bvzp vcxg') # email account and 3rd party app password for the account which the email will be sent from
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return "Email sent, the admin will send you an email in the next 24 hours with a new password"
    except:
        return "Email failed to send, please try again later"

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
        server.login('pathfinder3068@gmail.com', 'aaiu vmwm bvzp vcxg') # email account and 3rd party app password for the account which the email will be sent from
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        success = {'success':'false'}

    return JsonResponse(success, safe=False)

