from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
from models.db import user

def index(request):
    context = {
        'judul':'Home',
        'Home':True,
    }
    
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