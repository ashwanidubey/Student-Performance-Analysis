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
#cur_dir=os.getcwd()
#content_list=os.listdir(cur_dir)
#for x in content_list:
#        if x.split('.')[-1]=='csv':
            #csv_files.append(x)
#            print(x)
#        else:
#            print("jai ho",x)
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
    q=models.QuestionBank.objects.get(q_id=q_nos[0])
    return render(request,'user_app/taketest.html',{'q':q,'n':0,'qn':1})
def predict(request):
    global regressor
    if request.method=='POST':
        #print(request.POST)
        x=[request.POST['coding'],request.POST['aptitude'],request.POST['technical'],request.POST['communication'],request.POST['core'],request.POST['presentation'],request.POST['academics'],request.POST['puzzel'],request.POST['english'],request.POST['programming'],request.POST['management'],request.POST['projects'],request.POST['internship'],request.POST['training'],request.POST['backlog']]
        print(x)
        xt=np.array(x).reshape(1,-1)
        pr=regressor.predict(xt)
        #print(xt,"uff",pr)
        data={'chance':pr[0]}
        return render(request,'user_app/predict.html',data)
def history(request):
    return render(request,'user_app/history.html')
def help(request):
    return render(request,'user_app/help.html')
def showquestion(request):

    global q_nos
    print(q_nos)
    if request.method=='POST':
        #print(q_nos)
        print(request.POST)
        id=int(request.POST['id'])+1
        print(id)
        q=models.QuestionBank.objects.get(q_id=q_nos[id])
        return render(request,'user_app/taketest.html',{'q':q,'n':id,'qn':id})
    if request.method=='GET':
        print("jai ho",request.GET)
        if ',' in  request.GET['id']:
            id=request.GET['id'].split(',')
            print(id,"saaaleeee")
            id=id[0]

            id=int(id)
        else :
            id=int(request.GET['id'])+1
        if id==10:
            id=0
        print("bro ",id)
        print(q_nos)
        q=models.QuestionBank.objects.get(q_id=q_nos[id])
        return render(request,'user_app/taketest.html',{'q':q,'n':id,'qn':id})
