from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index2(request):
    var1 = {'helpvar':'Help Page fromhelp.html'}

    return render(request,'second_app/help.html',context=var1)