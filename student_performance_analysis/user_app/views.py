from django.shortcuts import render




def home(request):
    return render(request,'user_app/index.html')
def myform(request):
    return render(request,'user_app/myform.html')
def taketest(request):
        return render(request,'user_app/taketest.html')
