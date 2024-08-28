from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects_show = [
        {
            'title':'Chat_app',
            'path':'images/Chat_app.png'
        },
        {
            'title':'DRF_authentication',
            'path':'images/authentication.png'
        },
        {
            'title':'Django_Portfolio',
            'path':'images/portfolio.png'
        },
        {
            'title':'CRUD',
            'path':'images/crud.jpg'
        },
        {
            'title':'Ecommerce',
            'path':'images/ecommerce.jpg'
        },
    ]

    return render(request, 'projects.html', {"projects_show":projects_show})

def experiences(request):
    experiences = [
        {"company":"Company_name",
         "position":"python developer"},
        {"company":"Company_name1",
         "position":"python developer1"},
        {"company":"Company_name2",
         "position":"python developer2"},
    ]
    return render(request, 'experiences.html', {"experiences":experiences})

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphone = request.POST.get('phone')
        fmessage = request.POST.get('msg')
        query = Contact(name=fname, email=femail, phone=fphone, message=fmessage)
        query.save()

        # send email
        send_mail(
            'Message from: ' + femail + '| Name: ' + fname + '| Phone: ' + fphone,
            'Text: ' + fmessage,
            femail,
            [settings.EMAIL_HOST_USER]
        )
        messages.info(request, 'Thanks For Contacting Me!')
        return redirect('/contact')
    return render(request, 'contact.html')


def resume(request):
    resume_path = "myapp/resume.docx"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/docx")
            response['Content-Disposition']='attachment'; filename='resume.docx'
            return response
        
    else:
        return HttpResponse("resume not found", status=404)