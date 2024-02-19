from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from app.models import usr_reg


def home(request):
    return render(request,"index.html")

def login(request):
    
    return render(request,"login.html")
    
def register(request):
    
    return render(request,"register.html")


def register_save(request):
        n=''
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            passwd=request.POST.get('passwd')

            en=usr_reg(name=name, email=email,passwd=passwd)
            en.save()
            n="registration success"
        else:
            error="REGISTRATION FALD"
        return render(request,"login.html",{'n':n})    
            
    


def reset(request):
    return render(request,"reset.html")