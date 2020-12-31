from django.shortcuts import render
from . import  models
import random
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
    q=models.QuestionBank.objects.filter(q_id=q_nos[0])
    return render(request,'user_app/taketest.html',{'q':q})
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
def showquestion(request):
      q=models.QuestionBank.objects.filter(q_id=q_nos[1])
      return render(request,'user_app/taketest.html',{'q':q})
