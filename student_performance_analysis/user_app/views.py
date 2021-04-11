import os
from django.shortcuts import render
from . import  models
import random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime ,timedelta
#from rest_framework.views import APIView
#from rest_framework.response import response

df=pd.read_csv('mydataset.csv')
xdata=df.iloc[:,0:-1].values
ydata=df.iloc[:,-1].values
x_train,x_test,y_train,y_test=train_test_split(xdata,ydata,test_size=.2,random_state=1)
regressor=RandomForestRegressor(n_estimators=50,random_state=0)
regressor.fit(x_train,y_train)

q_nos=list()
pointer=0
# def addc(request):
#     q=models.ProgrammingLogic(q_id=31,question="q",opA="a",opB="b",opC="c",opD="d",answer="answer")
#     q.save()
    #return render(request,'user_app/index.html')
def home(request):
    return render(request,'user_app/index.html')
def myform(request):
    return render(request,'user_app/myform.html')
def taketest1(request):
     global q_nos
     q_nos.clear()
     start_time=datetime.now()
     end_time= start_time + timedelta(minutes = 1)
     difference_time=str(end_time-start_time).split(":")
     print("jai ho",difference_time)
     print("jai ho",difference_time[1])
     print("jai ho",difference_time[2])
     randlist=random.sample(range(1,40),10)
     randlist.sort()
     for i in range(0,10):
         q_nos.append(randlist[i])
    # print(q_nos)
     q=models.Aptitude.objects.get(q_id=q_nos[0])
    # return render(request,'user_app/taketest.html',{'q':q,'n':0,'qn':1})
     print("answer"+q.answer)
     data={'q':q,'qn':1,"type":"apti",'apt':1,'score':0,'prog':0,'comm':0,'apti':0,'year':end_time.year,'month':end_time.month,'day':end_time.day,'hour':end_time.hour,'minute':end_time.minute,'second':end_time.second,'pm':difference_time[1],'ps':difference_time[2]}
     return render(request,'user_app/taketest1.html',data)
def predict(request):
    global regressor
    if request.method=='POST':
        x=[request.POST['coding'],request.POST['aptitude'],request.POST['technical'],request.POST['communication'],request.POST['core'],request.POST['presentation'],request.POST['academics'],request.POST['puzzel'],request.POST['english'],request.POST['programming'],request.POST['management'],request.POST['projects'],request.POST['internship'],request.POST['training'],request.POST['backlog']]
        xt=np.array(x).reshape(1,-1)
        pr=regressor.predict(xt)
        p=pr[0]
        #data={'coding':x[0],'aptitude':x[1],'technical':x[2],'communication':x[3],'core':x[4],'presentation':x[5],'academics':x[6],'puzzel':x[7],'english':x[8],'programming':x[9],'management':x[10],'projects':x[11],'internship':x[12],'training':x[13],'backlog':x[14]}
        if p<50:
            c="only"
            if p<30:
                s="sorry to say but you cannot get placement with this skills"
            else:
                s="you are not in safe zone , keep learning"
            data={'chance':p,'slogan':s,'c':c,'coding':x[0],'aptitude':x[1],'technical':x[2],'communication':x[3],'core':x[4],'presentation':x[5],'academics':x[6],'puzzel':x[7],'english':x[8],'programming':x[9],'management':x[10],'projects':x[11],'internship':x[12],'training':x[13],'backlog':x[14]}
        else:
            c=""
            if p<75:
                s="keep it up"
            else:
                s="wish you for a bright future"
            data={'chance':p,'slogan':s,'c':c,'coding':x[0],'aptitude':x[1],'technical':x[2],'communication':x[3],'core':x[4],'presentation':x[5],'academics':x[6],'puzzel':x[7],'english':x[8],'programming':x[9],'management':x[10],'projects':x[11],'internship':x[12],'training':x[13],'backlog':x[14]}
        return render(request,'user_app/predict.html',data)
def history(request):
    return render(request,'user_app/history.html',{'val':1})
def help(request):
    return render(request,'user_app/help.html')
def showquestion(request):
    global q_nos
    if request.method=='POST':
        print(request.POST)
        #print(request.POST['type'])
        #type=request.POST['type']
        if request.POST['type']=='apti':
           if request.POST['timesup']=='1':
               score=int(request.POST['score'])
               prog=int(request.POST['prog'])
               apti=int(request.POST['apti'])
               comm=int(request.POST['comm'])
               start_time=datetime.now()
               end_time= start_time + timedelta(minutes = 1)
               difference_time=str(end_time-start_time).split(":")
               q_nos.clear()
               randlist=random.sample(range(1,40),10)
               randlist.sort()
               for i in range(0,10):
                   q_nos.append(randlist[i])
               print(0)
               print(q_nos[0])
               q=models.Communication.objects.get(q_id=q_nos[0])
               return render(request,'user_app/taketest1.html',{'q':q,'qn':1,"type":"comm",'verb':2,'score':score,'prog':prog,'comm':comm,'apti':apti,'year':end_time.year,'month':end_time.month,'day':end_time.day,'hour':end_time.hour,'minute':end_time.minute,'second':end_time.second,'pm':difference_time[1],'ps':difference_time[2]})
           else :
            qn=int(request.POST['qn'])
            score=int(request.POST['score'])
            prog=int(request.POST['prog'])
            apti=int(request.POST['apti'])
            comm=int(request.POST['comm'])
            op=str(request.POST['op'])
            answer=str(request.POST['answer'])
            if op==answer:
                print("jai ho")
                score+=1
                apti+=1
            print(answer)
            print(op)
            print("score ",score)
            if qn>=10:
                 start_time=datetime.now()
                 end_time= start_time + timedelta(minutes = 1)
                 difference_time=str(end_time-start_time).split(":")
                 q_nos.clear()
                 randlist=random.sample(range(1,40),10)
                 randlist.sort()
                 for i in range(0,10):
                     q_nos.append(randlist[i])
                 print(0)
                 print(q_nos[0])
                 q=models.Communication.objects.get(q_id=q_nos[0])
                 print("line n0 109 answer ",end_time.year,end_time.month,end_time.day,end_time.hour,end_time.minute,end_time.second)
                 return render(request,'user_app/taketest1.html',{'q':q,'qn':1,"type":"comm",'verb':2,'score':score,'prog':prog,'comm':comm,'apti':apti,'year':end_time.year,'month':end_time.month,'day':end_time.day,'hour':end_time.hour,'minute':end_time.minute,'second':end_time.second,'pm':difference_time[1],'ps':difference_time[2]})
            else:
                print(qn)
                print(q_nos[qn])
                year=request.POST['year']
                month=request.POST['month']
                day=request.POST['day']
                hour=request.POST['hour']
                minute=request.POST['minute']
                second=request.POST['second']
                start_time=datetime.now()
                end_time= datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
                difference_time=str(end_time-start_time).split(":")
                q=models.Aptitude.objects.get(q_id=q_nos[qn])
                print("answer "+q.answer)
                return render(request,'user_app/taketest1.html',{'q':q,'qn':qn+1,"type":"apti",'apt':1,'score':score,'prog':prog,'comm':comm,'apti':apti,'year':year,'month':month,'day':day,'hour':hour,'minute':minute,'second':second,'pm':difference_time[1],'ps':difference_time[2].split(".")[0]})


        elif  request.POST['type']=='comm':
          if request.POST['timesup']=='1':
              score=int(request.POST['score'])
              prog=int(request.POST['prog'])
              comm=int(request.POST['comm'])
              apti=int(request.POST['apti'])
              start_time=datetime.now()
              end_time= start_time + timedelta(minutes = 1)
              difference_time=str(end_time-start_time).split(":")
              q_nos.clear()
              randlist=random.sample(range(1,40),10)
              randlist.sort()
              for i in range(0,10):
                  q_nos.append(randlist[i])
              q=models.ProgrammingLogic.objects.get(q_id=q_nos[0])
              question=q.question.split('$')
              return render(request,'user_app/taketest1.html',{'question':question,'qq':q,'qnn':1,"type":"prog",'progg':3,'score':score,'prog':prog,'comm':comm,'apti':apti,'year':end_time.year,'month':end_time.month,'day':end_time.day,'hour':end_time.hour,'minute':end_time.minute,'second':end_time.second,'pm':difference_time[1],'ps':difference_time[2]})
                #return render(request,'user_app/taketest1.h
          else:
            qn=int(request.POST['qn'])
            score=int(request.POST['score'])
            prog=int(request.POST['prog'])
            comm=int(request.POST['comm'])
            apti=int(request.POST['apti'])
            op=str(request.POST['op'])
            answer=str(request.POST['answer'])
            if op==answer:
                score+=1
                comm+=1
            print(op)
            print(answer)
            print(comm)
            if qn>=10:
                 start_time=datetime.now()
                 end_time= start_time + timedelta(minutes = 1)
                 difference_time=str(end_time-start_time).split(":")
                 q_nos.clear()
                 randlist=random.sample(range(1,40),10)
                 randlist.sort()
                 for i in range(0,10):
                     q_nos.append(randlist[i])
                 print(0)
                 print(q_nos[0])
                 q=models.ProgrammingLogic.objects.get(q_id=q_nos[0])
                 question=q.question.split('$')
                 print("line no 153",end_time.year,end_time.hour)
                 return render(request,'user_app/taketest1.html',{'question':question,'qq':q,'qnn':1,"type":"prog",'progg':3,'score':score,'prog':prog,'comm':comm,'apti':apti,'year':end_time.year,'month':end_time.month,'day':end_time.day,'hour':end_time.hour,'minute':end_time.minute,'second':end_time.second,'pm':difference_time[1],'ps':difference_time[2]})
                  #return render(request,'user_app/taketest1.html',{'q':q,'qnn':1,"type":"prog",'prog':3})
            else:
              print(qn)
              print(q_nos[qn])
              year=request.POST['year']
              month=request.POST['month']
              day=request.POST['day']
              hour=request.POST['hour']
              minute=request.POST['minute']
              second=request.POST['second']
              start_time=datetime.now()
              print("line np 166 ",int(year),int(month),int(day),int(hour),int(minute),int(second))
              end_time= datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
              #end_time=datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

              difference_time=str(end_time-start_time).split(":")
              q=models.Communication.objects.get(q_id=q_nos[qn])
              print("answer "+q.answer)
              return render(request,'user_app/taketest1.html',{'q':q,'qn':qn+1,"type":"comm",'verb':2,'score':score,'prog':prog,'comm':comm,'apti':apti,'answer':q.answer,'year':year,'month':month,'day':day,'hour':hour,'minute':minute,'second':second,'pm':difference_time[1],'ps':difference_time[2].split(".")[0]})
        else:
          if request.POST['timesup']=='1':
              score=int(request.POST['score'])
              apti=int(request.POST['apti'])
              prog=int(request.POST['prog'])
              comm=int(request.POST['comm'])
              return render(request,'user_app/result.html',{'score':score,'prog':prog,'comm':comm,'apti':apti})

          else:
            qnn=int(request.POST['qnn'])
            score=int(request.POST['score'])
            apti=int(request.POST['apti'])
            prog=int(request.POST['prog'])
            comm=int(request.POST['comm'])
            op=str(request.POST['op'])
            answer=str(request.POST['answer'])
            if op==answer:
                score+=1
                prog+=1
            print(op)
            print(answer)
            print(prog)
            if qnn>=10:
                 return render(request,'user_app/result.html',{'score':score,'prog':prog,'comm':comm,'apti':apti})
            else :
               year=request.POST['year']
               month=request.POST['month']
               day=request.POST['day']
               hour=request.POST['hour']
               minute=request.POST['minute']
               second=request.POST['second']
               start_time=datetime.now()
               end_time=datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
               difference_time=str(end_time-start_time).split(":")
               print(qnn)
               print(q_nos[qnn])
               q=models.ProgrammingLogic.objects.get(q_id=q_nos[qnn])
               question=q.question.split('$')
               print("answer "+q.answer)
               return render(request,'user_app/taketest1.html',{'question':question,'qq':q,'qnn':qnn+1,"type":"prog",'progg':3,'score':score,'prog':prog,'comm':comm,'apti':apti,'year':year,'month':month,'day':day,'hour':hour,'minute':minute,'second':second,'pm':difference_time[1],'ps':difference_time[2].split(".")[0]})
