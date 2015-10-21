from django.contrib.auth.models import User
from django.db import models
import re
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

user_re=re.compile(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$')

charset=[chr(i) for i in set().union(*[
        range(ord('A'),ord('Z')+1),range(ord('a'),ord('z')+1),range(ord('0'),ord('9')+1)])]



class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username',
                'email',
                'password',
        ]
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Use letters, numbers and period(.)'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter a valid email id'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Password must be 6-30 character long'})
        }
        labels={
            'email':_('Email*')
        }
        help_texts = {
            'username': _(' '),
        }
    conf=forms.CharField(label='Confirm Password',widget=
            forms.PasswordInput(attrs={'placeholder':'Repeat the password entered'}),max_length=30)


    def clean_username(self):
        try:
            user=User.objects.get(username__iexact=self.cleaned_data.get('username'))
        except User.DoesNotExist:
            user=self.cleaned_data.get('username')
            if user[0] not in charset :
                raise forms.ValidationError("Username must start with alphanumeric character")
            if user[-1] not in charset :
                raise forms.ValidationError("Username must end with alphanumeric character")
            if not user_re.match(user):
                raise forms.ValidationError("Numbers, letters and period(.) are allowed. Can't start with period")
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('This field is required')
        try:
            email=User.objects.get(email__exact=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("The email is already registered. click Sign in to log into your account. Click forget password if you don't remember your password")

    def clean_password(self):
        pw=self.cleaned_data.get('password')
        if len(pw)<6:
            raise forms.ValidationError("password must be at least 6 character long")
        return pw
    def clean_conf(self):
        pw=self.cleaned_data.get("password")
        cnf=self.cleaned_data.get("conf")
        if pw!=cnf:
             raise forms.ValidationError("Confirm password Doesnt Match with password")
        return pw,cnf

class LogInForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs=
            {'placeholder':'Enter your Username'}))
    password=forms.CharField(required=False,max_length=30,widget=forms.PasswordInput(attrs=
        {'placeholder':'Enter your Password'}))

    def clean_username(self):
        user=self.cleaned_data.get('username')
        if not user_re.match(user):
            raise forms.ValidationError("Enter a valid Username")
        else:
            try:
                user=User.objects.get(username__iexact=self.cleaned_data.get('username'))
            except User.DoesNotExist:
                raise forms.ValidationError("Sorry, this username is not registered. Enter a valid username or Sign Up")
        return self.cleaned_data['username']

    def clean(self):
        try:
            self.clean_username()
        except:
            return None
        user=self.cleaned_data.get('username')
        pw=self.cleaned_data.get('password')
        user = authenticate(username=user, password=pw)
        if user:
            if user.is_active:
                return user,pw
            raise forms.ValidationError("The account is not yet acctivate. Check your email for activation link")
            return user,pw
        raise forms.ValidationError("Incorrect Password. Put your correct password")


class ForgetpwForm(forms.Form):
    username=forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs=
            {'placeholder':'Enter your Username'}))
    email=forms.EmailField(required=False,max_length=30,widget=forms.PasswordInput(attrs=
        {'placeholder':'Enter your email id'}))

    def clean_username(self):
        user=self.cleaned_data.get('username',None)
        if user:
            if not user_re.match(user):
                raise forms.ValidationError("Enter a valid Username")
            else:
                try:
                    user=User.objects.get(username__iexact=user)
                except User.DoesNotExist:
                    raise forms.ValidationError("Sorry, this username is not registered. Enter a valid username or Sign Up")
        return user

    def clean_email(self):
        email=self.cleaned_data.get('email',None)
        if email:
            try:
                email=User.objects.get(email__exact=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Sorry, this email id is not registered. Enter a valid email id or Sign Up")

    def clean(self):
        try:
            self.clean_username()
            self.clean_email()
        except:
            return None
        user=self.cleaned_data.get('username',None)
        email=self.cleaned_data.get('password',None)
        if not (user or email):
            raise forms.ValidationError("At least one of username and email must be mentioned")
        return user,pw

class NewpwForm(forms.Form):
    password=forms.CharField(required=False,max_length=30,widget=forms.PasswordInput(attrs=
        {'placeholder':'Enter your Password'}))
    repeat=forms.CharField(required=False,max_length=30,widget=forms.PasswordInput(attrs=
        {'placeholder':'Repeat your chosen Password'}))

    def clean_password(self):
        pw=self.cleaned_data.get('password')
        if len(pw)<6:
            raise forms.ValidationError("password must be at least 6 character long")
        return pw
    def clean_repeat(self):
        pw=self.cleaned_data.get("password")
        repeat=self.cleaned_data.get("repeat")
        if pw!=repeat:
             raise forms.ValidationError("Confirm password Doesnt Match with password")
        return pw,repeat
