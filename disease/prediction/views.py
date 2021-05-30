from django.shortcuts import render
from .models import Person
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def mailer(request):
    if(request.method=="POST"):
        name=request.POST.get("fn")+request.POST.get("ln")
        one=int(request.POST.get("one"))
        two=int(request.POST.get("two"))
        three=int(request.POST.get("three"))
        four=int(request.POST.get("four"))
        five=int(request.POST.get("fifth"))



def home(request):
    f=Person.objects.all()
    print(f)
    return render(request,'prediction/home.html',{'f':f})

def general(request):
    return render(request,'prediction/general.html',{})

def prediction(request):

    name=""

    one=request.POST.get("one")
    two=request.POST.get("two")
    three=request.POST.get("three")
    four=request.POST.get("four")
    five=request.POST.get("fifth")

    if(request.method=="POST"):
        name=request.POST.get("fn")+request.POST.get("ln")
        one=int(request.POST.get("one"))
        two=int(request.POST.get("two"))
        three=int(request.POST.get("three"))
        four=int(request.POST.get("four"))
        five=int(request.POST.get("fifth"))

    lis=[[one,two,three,four,five]]
    
    data = open(os.path.join(BASE, 'ap_train.csv'))
    xtrain=pd.read_csv(data)

    ytrain=xtrain['target'].values

    xtrain=xtrain.drop('target',axis=1)

    
    ytrain=pd.DataFrame(ytrain,columns=['target'])

    # xtest=pd.read_csv('ap_test.csv')
    xtrain=xtrain.values
    ytrain=ytrain.values
    model = LinearRegression()
    model.fit(xtrain,ytrain)
    model.predict([xtrain[0],xtrain[1]])
    score=model.score(xtrain,ytrain)
    xtest=lis
    ans=[]
    idx=[]
    k=0
    # t=[xtest[i] for i in range(len(xtest))]
    # idx=[i for i in range(len(xtest))]
    ans=model.predict(xtest)

    print(ans)
    
    return render(request,'prediction/home.html',{'ans':ans,'score':score})

# ##################
# from django.http import HttpResponse
# import csv

# def download(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['UserId','Name', 'DOB', 'Joining Data'])

#     users = Person.objects.all().values_list('id','name', 'dob', 'regdate')
#     for user in users:
#         writer.writerow(user)

#     return response
# ############

# def anon(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['UserId', 'DOB', 'Joining Data'])

#     users = Person.objects.all().values_list('id', 'dob', 'regdate')
#     for user in users:
#         writer.writerow(user)

#     return response