from django.core.mail import send_mail
from django.template import Context, Template
from hashlib import md5



subject_template=Template("Complete Registration for {{ site.name }}")
text_template=Template("""{% load i18n %}
{% trans "Activate account at" %} {{ site.name }}:

Hello there!

Click the link below to activate your account.


http://{{ site.domain }}{% url 'registration_activate' user activation %}


{% blocktrans %}The above link is valid for {{ expiration_days }} days.{% endblocktrans %}

-Team {{teamname}}""")


def registration_email(site,username,email):
    context=Context({'site':site,
             'activation':md5(username+md5('Aryabhaskar').hexdigest()).hexdigest(),
             'expiration_days':7,'teamname':'Aryabhaskar','user':username,'url':'/profile'
             })

    send_mail(subject_template.render(context),text_template.render(context), 'suppost@aryabhaskar.com',
        [email], fail_silently=False)

def fpw_email(site,username,email):
    subject_template=Template("Reset Password for your {{ site.name }} account")
    text_template=Template("""{% load i18n %}
    {% trans "Reset password for your account at" %} {{ site.name }}:

    Hello {{username}}

    Click the link below to Reset your account password.


    http://{{ site.domain }}{% url 'new_pw' user activation %}


    {% blocktrans %}The above link is valid for {{ expiration_days }} days.{% endblocktrans %}

    -Team {{teamname}}""")

    context=Context({'site':site,
             'activation':md5(username+md5('reset_pw').hexdigest()).hexdigest(),
             'expiration_days':7,'teamname':'Aryabhaskar','user':username,'url':'/profile'
             })

    send_mail(subject_template.render(context),
              text_template.render(context),
              'support@aryabhaskar.com',
        [email], fail_silently=False)