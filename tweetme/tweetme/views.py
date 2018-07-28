from django.shortcuts import render


def home(request):
    return render(request,'home.html',{})

def aboutme(request):
    return render(request,'tweets/aboutme.html',{})
