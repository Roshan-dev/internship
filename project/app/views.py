from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from project import settings
from django.contrib import messages
from.models import Contact
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=="POST":
        fullname =request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        description=request.POST.get('description')
        contact_query = Contact(name=fullname,email=email,number=phone,description=description)
        contact_query.save()
        from_email=settings.EMAIL_HOST_USER
        #email starts here
        connection=mail.get_connection()
        connection.open()
        email_mesge=mail.EmailMessage(fullname,description,from_email=['devroshan666@gmail.com'],connection=connection)
        email_user=mail.EmailMessage([email_mesge])
        connection.send_messages([email_mesge,email_user])
        connection.close()
        messages.info(request,"Thanks for contacting us")
        return redirect('/contact')
        
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def handleBlog(request):
    if  not request.user.is_authenticated:
        messages.error(request,"please login and try again")
        return  redirect('/login')
    return render(request,'handleBlog.html')
def about(request):
    return render(request,'about.html')
def signUp(request):
    if request.method == "POST":
        username=request.POST['username']
        firstname =request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1!=pass2:
            return HttpResponse("password not matched")
        try:
            if user.objects.get(username=username):
                return HttpResponse("username is taken")
        except Exception as identifier:
            pass
        try:
            if user.objects.get(email=email):
                return HttpResponse("email is already taken")
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=firstname
        myuser.last_nane=lastname
        myuser.save()
        return HttpResponse("signup successfully")
    return render(request,'auth/signUp.html')
def handlelogin(request):
    if request.method == "POST":
        handleusername=request.POST['username']
        handlepassword =request.POST['pass1']
        user=authenticate(username=handleusername,password=handlepassword)
        if user is not None:
            login(request,user)
            messages.info(request,'Welcome to my Website')
            return redirect('/')
        else:
            messages.warning(request,"Invalid credentials")
            return redirect('/login')
    return render(request,'auth/login.html')
def handlelogout(request):
    logout(request)
    messages.success(request,"logout success")
    return redirect('/login')