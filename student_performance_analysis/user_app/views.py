from django.shortcuts import render
from . import  models
import random


def home(request):
    return render(request,'user_app/index.html')
def myform(request):
    return render(request,'user_app/myform.html')
def taketest(request):
    randlist=random.sample(range(1,40),10)
    randlist.sort()
    for i in range(1,10):
        q2=models.QuestionBank.objects.filter(q_id=randlist[i])
        q1 = q1.union(q2)
    return render(request,'user_app/taketest.html',{'q':q1})
def predict(request):
    if request.method=='POST':
        print(request.POST)
        data={'name':request.POST['yourname'],'email':request.POST['youremail'],'cpi':request.POST['yourpercent13'],'branch':request.POST['yourbranch'],'gender':request.POST['yourgender'],'inter':request.POST['yourpercent12'],'highschool':request.POST['yourpercent10'],'currentback':request.POST['yourcb'],'everback':request.POST['youreb'],'project':request.POST['yourproject'],'techevent':request.POST['yourte'],'techquiz':request.POST['yourtq']}
        for x in data:
            print(x," ",data[x])
        return render(request,'user_app/predict.html',data)
def history(request):
    return render(request,'user_app/history.html')
def help(request):
    return render(request,'user_app/help.html')
