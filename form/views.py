from django.forms.forms import Form
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import mysql.connector
from django.contrib import messages
#from django.contrib.auth.models import user
from .models import user
from operator import itemgetter

# Create your views here.
       
def indexView(request):
    return render(request, 'index.html')

@login_required
def login(request):
    con = mysql.connector.connect(host="localhost", user="root",passwd="root",database="login", port="3306")
    cursor= con.cursor()
    con2 = mysql.connector.connect(host="localhost", user="root",passwd="root",database="login", port="3306")
    cursor2= con2.cursor()
    sqlcommand = "select email from task_user"
    sqlcommand2 = "select password from task_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    print(res)
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        i=1
        k=len(res)
        while i<k:
            if res[i] == email and res2[i]==password:
                return render(request,'indexview.html',{'email':email})

                break
            i+=1
        else:
                messages.info(request,"check username and passsword")
                return redirect('login')
    return render(request,'login.html')

def registerView(request):
    if request.method == "POST":
        User = user()
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('task_url')
       
        user.username = request.POST['username']
        user.email = request.POST['Email']
        user.password = request.POST['Password1']
        user.repassword = request.POST['Password2']
        user.address = request.POST['address']
        if user.password != user.repassword:
            return redirect('register')
        elif user.username == "" or user.password == "":
            messages.info(request,'some field are empty')
            return redirect('register')
        else:
            user.save()   
    return render(request, 'registration/register.html')
    