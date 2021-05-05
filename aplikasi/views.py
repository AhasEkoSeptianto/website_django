from django.shortcuts import render,redirect
from .models import postModel
from .forms import postForm
from PIL import Image

# Create your views here.
def index(request):
    semua = postModel.objects.all()
    context = {
        'judul':'aplikasi',
        'semua':semua,
        'Aplikasi':True,
    }

    return render(request, 'aplikasi/index.html',context)

def add(request):
    
    form = postForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():

            # check if image field == True
            gambar = request.FILES['gambaraplikasi']
            hasil = Image.open(gambar)
            error = ''
            # file is saved
            form.save()
        else :

            error = 'gambaraplikasi hanya dapat berisi gambar'
            print(error)
        return render(request,'aplikasi/add.html',{'form':form,'error':error})

    return render(request, 'aplikasi/add.html', {'form': form})

def listdata(request, data):
    semualist = postModel.objects.get(slug=data)
    context = {
        'judul':'List Aplikasi',
        'tambah':semualist,
        'Aplikasi':True,
    }

    return render(request, 'aplikasi/listdata.html', context)