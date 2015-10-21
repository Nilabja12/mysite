from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.sites.models import Site,get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *
from .functions import registration_email,fpw_email

from hashlib import *


def SignUp(request):
#    site = RequestSite(request)
#    print site
    site = Site.objects.get_current()
    form =SignUpForm(request.POST or None)
    if form.is_valid():
        instance=form.save()
        instance.username=instance.username.lower()
        instance.set_password(instance.password)
        instance.is_active=False
        instance.save()
        registration_email(site,instance.username,instance.email)
        return  HttpResponseRedirect('registration_complete')
    variables ={
    'form': form
    }

    return render(request,
    'signup.html',
    variables
    )
def Reg_Complete(request):
    site = Site.objects.get_current()
    return render(request,'reg_complete.html',{'site':site})
def Activate(request,user,act):
    print user
    print act
    try:
        a=User.objects.get(username__exact=user)
    except User.DoesNotExist:
        return render (request,'serror.html')
    if md5(user+md5('Aryabhaskar').hexdigest()).hexdigest()!=act:
         return render (request,'serror.html')
    a.is_active=True
    a.save()
    url = reverse('activ_success')
    return HttpResponseRedirect(url)
#
#def dashboard(request,user):
#    context={'title':user,'user':user}
#    return render(request,'dashboard.html',context)

def Activ_succ(request):
    return render(request, 'activ_success.html')



def Login(request):
    if request.user.is_authenticated():
        print "authenticated"
        return HttpResponseRedirect(reverse("dashboard"))
    form=LogInForm(request.POST or None)
    if form.is_valid():
        usr = request.POST.get('username')
        pw = request.POST.get('password')
        rem=request.POST.get('rem_me',None)
        print usr,pw
        user = authenticate(username=usr, password=pw)
        print user
        if user is not None:
            if user.is_active:
                if not rem:
                    request.session.set_expiry(0)
                login(request, user)
                print "logged in"
                return HttpResponseRedirect(reverse("dashboard"))
            else:
                print 'user not active'
        else:
            print 'not authenticated'

    variables ={
     'title':'Log In',
     'form': form
    }

    return render(request,
    'login.html',
    variables
    )

def Dashboard(request):
    if request.user.is_authenticated():
        return HttpResponse("Welcome {user}".format(user=request.user))
    else:
        print "Not authenticated"
        return HttpResponseRedirect(reverse("login"))

def Logout(request):
    logout(request)
    url=reverse("home")
    return HttpResponseRedirect(url)
def Forgot_PW(request):
    site = Site.objects.get_current()
    form =ForgetpwForm(request.POST or None)
    if form.is_valid():
        email=request.POST.get('email',None)
        user=request.POST.get('username',None)
        if not email:
            user=user.lower()
            email=User.objects.get(username__iexact=user).email
        fpw_email(site,user,email)
        return  HttpResponseRedirect('forgot_pw_cmplt')
    variables ={
    'form': form,
    'title':'Forgot Password'
    }

    return render(request,'forgot.html',variables)

def New_PW(request,user,act):
    print user
    print act
    try:
        a=User.objects.get(username__exact=user)
    except User.DoesNotExist:
        return render (request,'serror.html')
    if md5(user+md5('reset_pw').hexdigest()).hexdigest()!=act:
         return render (request,'serror.html')
    form =NewpwForm(request.POST or None)
    if form.is_valid():
        pw=request.POST.get('password',None)
        a.set_password(pw)
        a.save()
        return  HttpResponseRedirect(reverse('dashboard'))
    variables ={
    'form': form
    }

    return render(request,
    'forgot.html',
    variables
    )
