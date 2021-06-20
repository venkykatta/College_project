from django.shortcuts import render
from django.http import HttpResponse
from user.models import *
from user.forms import *
from manager.models import *
from manager.forms import *
from django.contrib import messages
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from django_pandas.io import read_frame
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score




def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin/adminloginentered.html")

def userdetails(request):
    qs=userModel.objects.all()
    print("qs",qs)
    return render(request,"admin/userdetails.html",{"qs":qs})

def managerdetails(request):
    qs=managerModel.objects.all()
    return render(request,"admin/managerdetails.html",{"qs":qs})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        userModel.objects.filter(id=uname).update(status=status)
        qs=userModel.objects.all()
        return render(request,"admin/userdetails.html",{"qs":qs})


def activatemanager(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        managerModel.objects.filter(id=uname).update(status=status)
        qs=managerModel.objects.all()
        return render(request,"admin/managerdetails.html",{"qs":qs})

def svm(request):
    qs = weightmodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    #data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    #print("data-label:",data.label)
    dataset = data.iloc[:,3:5].values
    print("x",dataset)
    dataset1 = data.iloc[:,4:5].values
    print("y",dataset1)
    print("shape",dataset.shape)
    X = dataset
    y = dataset1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=0)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    #print(svclassifier.predict([0.58, 0.76]))
    y_pred = svclassifier.predict(X_test)
    m = confusion_matrix(y_test, y_pred)
    accurancy = classification_report(y_test, y_pred)
    print(m)
    print(accurancy)
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {

        "m": m,
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        'len29': x[29],
        'len30': x[30],
        'len31': x[31],
        'len32': x[32],
        'len33': x[33],

    }
    return render(request, 'admin/accuracy.html', dict)


def xgboost(request):
    qs = weightmodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    # data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    # print("data-label:",data.label)
    dataset = data.iloc[:,3:4].values
    print("x", dataset)
    dataset1 = data.iloc[:,5].values
    print("y", dataset1)
    print("shape", dataset.shape)
    X = dataset
    #y = dataset1
    print(dataset.shape)
    # split data into X and y
    #X = dataset[:, 0:8]
    #Y = dataset[:, 8]
    #X = dataset
    print("X",len(X))
    Y = dataset1
    print("Y", len(Y))
    #print("x",X)
    # split data into train and test sets
    seed = 2
    test_size = 3
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
    """print("X_train",X_train)
    print(" X_test", X_test)
    print("y_train",y_train)
    print("y_test",y_test)"""
    # fit model no training data
    model = XGBClassifier()


    model.fit(X_train, y_train)
    # make predictions for test data
    y_pred = model.predict(X_test)
    print("y_pred",y_pred)
    predictions = [(value) for value in y_pred]
    print("predictions",predictions)
    # evaluate predictions
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    dict = {
            "accuracy" : accuracy* 100.0,
    }
    return render(request,"admin/xgboost.html",dict)

