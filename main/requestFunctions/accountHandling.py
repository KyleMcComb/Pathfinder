# below imports are used for sending an email
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from database.models import *
from mysite.settings import *
from main.forms import CustomLoginForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

'''
    @Author: @DeanLogan
    @Description: Gets the username and password from the request then checks if these credentials are on the system, returns true or false based on authentication result.
    @param: request -  HttpRequest object that contains metadata about the request
    @return: loggedIn - JSON object containing whether or not a the log in attempt was successful
'''
def verify(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password']))
            # Set session timeout based on 'remember_me' value
            if form.cleaned_data.get('remember_me', False):
                request.session.set_expiry(1209600)  # Two weeks (in seconds)
            return JsonResponse({'loggedIn': 'true'})
        else:
            return JsonResponse({'loggedIn': 'false', 'errors': form.errors})
    else:
        print("here")
        return JsonResponse({'errors': 'Invalid request method'})

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

