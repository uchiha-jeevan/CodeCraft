from django.shortcuts import render

# Create your views here.
from django.http import request


def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')


def here(request):
    return render(request,'here.html')

def basicmath(request):

    return render(request,'basicmath.html')

def add(request):
    a=int(request.POST.get('nu'))
    b=int(request.POST.get('mu'))
    r=a+b
    return render(request,'basicmath.html',{'result':r})

def sub(request):
    a=int(request.POST.get('ns'))
    b=int(request.POST.get('ms'))
    r=a-b
    return render(request,'basicmath.html',{'subresult':r})

def mul(request):
    a=int(request.POST.get('nl'))
    b=int(request.POST.get('ml'))
    r=a*b
    return render(request,'basicmath.html',{'mulresult':r})

def div(request):
    # a=int(request.POST.get('nd'))
    # b=int(request.POST.get('md'))
    # r=a%b
    # return render(request,'basicmath.html',{'div-result':r})

    if request.method == 'POST':
        nd = request.POST.get('nd')
        md = request.POST.get('md')
        if nd is not None and md is not None:
            a = int(nd)
            b = int(md)
            r = a % b
            rr=a/b
            return render(request, 'basicmath.html', {'divresult': r,'modresult':rr})
        else:
            # Handle the case where nd or md is missing
            # You can render an error message or redirect to another page
            pass
    # Handle GET request or invalid POST request
    return render(request, 'basicmath.html')


def returns(request):
    return render(request,'returns.html')