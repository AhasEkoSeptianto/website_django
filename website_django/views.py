from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
from models.db import user
import jwt

from helpers.getEnv import SECRET_JWT

def index(request):
    
    context = { 
        'judul':'Home',
        'Home':True,
    }
    
    print(request.user)
    # user = user
    # insert  = {
    #     'username': 'ahaseko1@gmail.com',
    #     'password': 'aaseko100465'
    # }

    # user.save(insert)

    # newData ={
    #     'email': 'ahaseko1@gmail.com',
    #     'name': 'ahaseko',
    #     'password': 'aaseko100465'
    # }

    # user.insert_one(newData)

    # cursor = user.find({})
    # for doc in cursor :
    #     print(doc)


    return render(request, 'index.html', context)

def loginuser(request):
    context = {
        'judul':'login',
        'Login':True,
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None :
            login(request, user)
            return redirect('index')

    return render(request, 'auth/login.html',context)

def logoutuser(request):
    logout(request)

    return redirect('index')

def galery(request):
    user = request.user.username
    # print(user)
    
    token = jwt.encode({"username": user}, SECRET_JWT)
    # print(token.decode('UTF-8'))
    # return redirect('index')
    return redirect('https://my-galerys.netlify.app/galery?token=' + token.decode('UTF-8'))
    # return redirect('http://localhost:3000/galery?token=' + token.decode('UTF-8'))
    