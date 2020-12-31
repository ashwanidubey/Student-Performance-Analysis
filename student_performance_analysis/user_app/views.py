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
    print(q_nos)
    q=models.QuestionBank.objects.get(q_id=q_nos[0])
    return render(request,'user_app/taketest.html',{'q':q,'n':0,'qn':1})
def predict(request):
    if request.method=='POST':

        data={'name':request.POST['yourname'],'email':request.POST['youremail'],'cpi':request.POST['yourpercent13'],'branch':request.POST['yourbranch'],'gender':request.POST['yourgender'],'inter':request.POST['yourpercent12'],'highschool':request.POST['yourpercent10'],'currentback':request.POST['yourcb'],'everback':request.POST['youreb'],'project':request.POST['yourproject'],'techevent':request.POST['yourte'],'techquiz':request.POST['yourtq']}

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
