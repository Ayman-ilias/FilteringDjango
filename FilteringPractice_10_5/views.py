from django.shortcuts import render

def home(request):
    d= {'name':'John Doe','age':30, 'lst' : ['python','django','java','ruby'],'s':'AMI KICHU PARINA'}
    # lst=['python','django','java','ruby']

    return render(request,'home.html',d)