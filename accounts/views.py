from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import DetailForm,CertificationForm
from .models import Bio,Billing
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail


def csignin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('Userdashboard')
        else:
            return render(request, 'accounts/Signin.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'accounts/Signin.html')


def isignin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('wupload')
        else:
            return render(request, 'accounts/Signin.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'accounts/Signin.html')


def isignup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            email = request.POST['Email']
            emailto = 'oladipupoemmanuel85@gmail.com'
            password = request.POST['password']
            field = request.POST['field']
            cert = request.POST['cert']
            subject = 'instructor account request'
            message = f'hi the following requests for an instructor account: {email} \n password:{password} \n field:{field} \n certification:{cert}'
            email_from = settings.EMAIL_HOST_USER
            recipient = [emailto,]
            send_mail(subject,message,email_from,recipient)
            mg = 'account request sent!'
            return render(request, 'accounts/InstructorSignup.html', {'mg': mg})
        else:
            mg = 'passwords must match'
            return render(request, 'accounts/InstructorSignup.html', {'mg': mg})
    else:
        return render(request, 'accounts/InstructorSignup.html')


def csignup(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['password']
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            u = User.objects.get(username=email)
            fname = 'N/A'
            sname = 'N/A'
            phone = 23480000000000000
            num = 'N/A'
            street = 'N/A'
            city = 'N/A'
            postal = 'N/A'
            state = 'N/A'
            country = 'N/A'
            b = Bio(firstname=fname,secondname=sname,phone=phone,username=u)
            b.save()
            bill = Billing(username=u,num=num,street=street,city=city,postal=postal,state=state,country=country)
            bill.save()
            return redirect('Signin')
        else:
            mg = 'passwords must match'
            return render(request, 'accounts/Signup.html', {'mg': mg})
    else:
        return render(request, 'accounts/Signup.html')


def Userdashboard(request):
    u = User.objects.get(username=request.user.get_username())
    bi = Bio.objects.get(username=u)
    bill = Billing.objects.get(username=u)
    return render(request, 'accounts/user-profile.html', {'u': u, 'bi': bi, 'bill': bill})


def updatebio(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['sname']
        phone = request.POST['phone']
        b = Bio(firstname=fname,secondname=sname,phone=phone,username=request.user.get_username())
        b.save()
        mg = 'bio updated!'
        return render('accounts/edit-userprofile.html', {'mg': mg})
    else:
        return render(request,'accounts/edit-userprofile.html')


def updateimage(request):
    if request.method == 'POST' and request.FILES['img']:
        img = request.FILES['img']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
        v = request.user.get_username()
        f = User.objects.get(username=v)
        Bio.objects.filter(username=f).update(image=file)
        u = User.objects.get(username=request.user.get_username())
        bi = Bio.objects.get(username=u)
        return render(request, 'accounts/edit-userprofile.html', {'bi': bi})
    else:
        u = User.objects.get(username=request.user.get_username())
        bi = Bio.objects.get(username=u)
        return render(request,'accounts/edit-userprofile.html', {'bi':bi})

def updatebilling(request):
    if request.method == 'POST':
        num = request.POST['num']
        street = request.POST['street']
        city = request.POST['city']
        postal = request.POST['postal']
        state = request.POST['state']
        country = request.POST['country']
        b = Billing.objects.get(username=request.user.get_username()).update(num=num,street=street,city=city,postal=postal,state=state,country=country)
        b.save()
        mg = 'billing updated!'
        return render(request,'accounts/edit-userprofile.html', {'mg': mg})
    else:
        return render(request,'accounts/edit-userprofile.html')


def faq(request):
    return render(request,'accounts/page-faq.html')


def pricing(request):
    return render(request,'accounts/page-pricing.html')


def term(request):
    return render(request,'accounts/page-term.html')


@login_required(login_url='accounts/Signin.html')
def usersettings_cp(request):
    if request.method == 'POST':
        u = request.user
        us = User.objects.get(username=u, password=request.POST['pass1'])
        if request.POST['pass2'] == request.POST['pass3']:
            us.set_password(request.POST['pass2'])
            us.save()
        else:
            mg = 'passwords must match'
            return render(request, 'accounts/cprofilesettings.html#security', {'mg': mg})
    else:
        return render(request, 'accounts/cprofilesettings.html#security')


@login_required(login_url='accounts/Signin.html')
def usersettings_delete(request):
    if request.method == 'POST':
        username = request.user
        try:
            u = User.objects.get(username=username)
            u.delete()
            msg = 'The user is deleted.'
            return render(request, 'accounts/signup.html', {'msg': msg})
        except Exception as e:
            print(e)
    else:
        return render(request, 'accounts/cprofilesettings#account.html')

