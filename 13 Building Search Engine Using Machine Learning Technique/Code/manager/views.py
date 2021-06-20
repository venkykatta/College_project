from django.shortcuts import render
from manager.models import *
from manager.forms import *
from user.models import *
from django.http import HttpResponse
from django.contrib import messages
from builtins import Exception
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from django_pandas.io import read_frame



def managerlogin(request):
    return render(request,'manager/managerlogin.html')


def managerregister(request):
    if request.method=='POST':
        form1=managerForm(request.POST)
        if form1.is_valid():
            form1.save()
            print("succesfully saved the data")
            return render(request, 'manager/managerlogin.html')
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=managerForm()
        return render(request,"manager/managerregister.html",{"form":form})


def managerlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        print(sname)
        spasswd = request.POST.get('upasswd')
        print(spasswd)
        try:
            check = managerModel.objects.get(email=sname,passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            # request.session['name'] = check.name
            # print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'manager/managerpage.html')
            else:
                messages.success(request, 'manager is not activated')
                return render(request, 'manager/managerlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'manager/managerlogin.html')



def fileupload(request):
    if request.method =='POST':
        form = UploadfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'manager/uploadfile.html')
    else:
        form=UploadfileForm()
    return render(request, 'manager/uploadfile.html',{'form':form})







