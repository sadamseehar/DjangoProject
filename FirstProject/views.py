from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("home function")

def home1(request):
    return render(request,'home.html')


def homedata(request):
    data = {
        'name':'Ahmed',
        'number':['123456','456789'],
        'dict':[{'age':'12','city':'khi'},
                {'age':'12','city':'khi'}
        ]
    }
    return render(request,"home.html",data)



def about(request):
    return render(request,"about.html")



def contact(request):
    return render(request,"contact.html")