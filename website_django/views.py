from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


def index(request):
    context = {
        'judul':'Home',
        'Home':True,
    }
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
        if user is not None :
            login(request, user)
            return redirect('index')

    return render(request, 'auth/login.html',context)

def logoutuser(request):
    logout(request)

    return redirect('index')