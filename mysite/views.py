from django.shortcuts import render


def home(request):
    context={'title':'Welcome | Mysite' }
    return render(request,'home.html',context)