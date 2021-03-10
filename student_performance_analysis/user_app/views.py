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
pointer=0

def home(request):
    return render(request,'user_app/index.html')
def myform(request):
    return render(request,'user_app/myform.html')
def taketest1(request):
     global q_nos
     q_nos.clear()
     randlist=random.sample(range(1,40),10)
     randlist.sort()
     for i in range(0,10):
         q_nos.append(randlist[i])
    # print(q_nos)
     q=models.Aptitude.objects.get(q_id=q_nos[0])
    # return render(request,'user_app/taketest.html',{'q':q,'n':0,'qn':1})
     return render(request,'user_app/taketest1.html',{'q':q,'qn':1,"type":"apti",'apt':1})
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
        print(request.POST)
        print(request.POST['type'])
        #type=request.POST['type']
        if request.POST['type']=='apti':
            qn=int(request.POST['qn'])
            if qn>=10:
                 q_nos.clear()
                 randlist=random.sample(range(1,40),10)
                 randlist.sort()
                 for i in range(0,10):
                     q_nos.append(randlist[i])
                 q=models.Communication.objects.get(q_id=q_nos[0])
                 return render(request,'user_app/taketest1.html',{'q':q,'qn':1,"type":"comm",'verb':2})
            else:
               q=models.Aptitude.objects.get(q_id=q_nos[qn])
               return render(request,'user_app/taketest1.html',{'q':q,'qn':qn+1,"type":"apti",'apt':1})
        elif  request.POST['type']=='comm':
            qn=int(request.POST['qn'])
            if qn>=10:
                 q_nos.clear()
                 randlist=random.sample(range(1,40),10)
                 randlist.sort()
                 for i in range(0,10):
                     q_nos.append(randlist[i])
                 q=models.ProgrammingLogic.objects.get(q_id=q_nos[0])
                 return render(request,'user_app/taketest1.html',{'q':q,'qnn':1,"type":"prog",'prog':3})
            else:
              q=models.Communication.objects.get(q_id=q_nos[qn])
              return render(request,'user_app/taketest1.html',{'q':q,'qn':qn+1,"type":"comm",'verb':2})
        else:
            qnn=int(request.POST['qnn'])
            if qnn>=10:
                 score=0;
                 return render(request,'user_app/result.html',{"score":score})
            else :
               q=models.ProgrammingLogic.objects.get(q_id=q_nos[qnn])
               print(q.question)
               question=q.question.split('$')
               for x in question :
                   print(x)
               return render(request,'user_app/taketest1.html',{'question':question,'qq':q,'qnn':qnn+1,"type":"prog",'prog':3})
