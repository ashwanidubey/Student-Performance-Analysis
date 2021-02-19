import os
from django.shortcuts import render
from . import  models
import random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv('mydataset.csv')
xdata=df.iloc[:,0:-1].values
ydata=df.iloc[:,-1].values
x_train,x_test,y_train,y_test=train_test_split(xdata,ydata,test_size=.2,random_state=1)
regressor=RandomForestRegressor(n_estimators=50,random_state=0)
regressor.fit(x_train,y_train)

q_nos=list()

def home(request):
    return render(request,'user_app/index.html')
def myform(request):
    return render(request,'user_app/myform.html')
def taketest(request):
    global q_nos
    q_nos.clear()
    randlist=random.sample(range(1,40),10)
    randlist.sort()
    for i in range(0,10):
        q_nos.append(randlist[i])
    print(q_nos)
    q=models.Aptitude.objects.get(q_id=q_nos[0])
    return render(request,'user_app/taketest.html',{'q':q,'n':0,'qn':1})
def predict(request):
    global regressor
    if request.method=='POST':
        x=[request.POST['coding'],request.POST['aptitude'],request.POST['technical'],request.POST['communication'],request.POST['core'],request.POST['presentation'],request.POST['academics'],request.POST['puzzel'],request.POST['english'],request.POST['programming'],request.POST['management'],request.POST['projects'],request.POST['internship'],request.POST['training'],request.POST['backlog']]
        xt=np.array(x).reshape(1,-1)
        pr=regressor.predict(xt)
        p=pr[0]
        if p<50:
            c="only"
            if p<30:
                s="sorry to say but you cannot get placement with this skills"
            else:
                s="you are not in safe zone , keep learning"
            data={'chance':p,'slogan':s,'c':c}
        else:
            if p<75:
                s="keep it up"
            else:
                s="wish you for a bright future"
            data={'chance':p,'slogan':s}
        return render(request,'user_app/predict.html',data)
def history(request):
    return render(request,'user_app/history.html')
def help(request):
    return render(request,'user_app/help.html')
def showquestion(request):
    global q_nos
    if request.method=='POST':
        id=int(request.POST['id'])+1
        q=models.Aptitude.objects.get(q_id=q_nos[id])
        return render(request,'user_app/taketest.html',{'q':q,'n':id,'qn':id})
    if request.method=='GET':
        if ',' in  request.GET['id']:
            id=request.GET['id'].split(',')
            id=id[0]
            id=int(id)
        else :
            id=int(request.GET['id'])+1
        if id==10:
            id=0
        q=models.Aptitude.objects.get(q_id=q_nos[id])
        return render(request,'user_app/taketest.html',{'q':q,'n':id,'qn':id})
