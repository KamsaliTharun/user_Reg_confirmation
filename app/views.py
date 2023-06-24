from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Create your views here.
from app.models import *
def registration(request):
    ufo = userform()
    Boolean=False
    d = {'ufo' : ufo,"Boolean":Boolean}
    if request.method == 'POST':
        d['Boolean']=True
        ufd = userform(request.POST)
        if ufd.is_valid():
            un=ufd.cleaned_data['username']
            d['b2']=False
            nsuo = ufd.save(commit = False)
            nsuo.set_password(ufd.cleaned_data['password'])
            nsuo.save()
            return render(request,'registration.html',d)
        else:
            d['b2']=True
            return render(request,'registration.html',d)
    return render(request, 'registration.html',d)

