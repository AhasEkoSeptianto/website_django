from django.shortcuts import render,redirect
from .forms import postForm
from .models import postModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request):
    context = {
        'judul':'report',
        'Report':True,
    }
    return render(request, 'report/index.html', context)

@login_required
def data(request,tahun,bulan):
    report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    context = {
        'judul':'report',
        'data':report,
        'bulan':bulan,
        'tahun':tahun,
        'Report':True,
    }
    return render(request, 'report/report.html', context)

@login_required
def datatambah(request,tahun,bulan):
    report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    data = {
        'tahun':tahun,
        'bulan':bulan,
        'tanggal':'',
        'body':'',    
        'Report':True,
    }
    
    post = postForm(request.POST or None,initial=data)
    if request.method == 'POST':
        if post.is_valid():
            post.save()

            return redirect('report:data',tahun,bulan)

    context = {
        'judul':'report',
        'data':report,
        'tahun':tahun,
        'bulan':bulan,
        'post':post,
        'Report':True,
    }
    
    return render(request, 'report/create.html', context)

@login_required
def viewupdate(request,tahun,bulan):
    report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    data = {
        'bulan':bulan,
        'tanggal':'',
        'body':'',    
        'Report':True,
    }
    
    post = postForm(request.POST or None,initial=data)
    if request.method == 'POST':
        if post.is_valid():
            post.save()

            return render(request,'report/update.html')

    context = {
        'tahun':tahun,
        'bulan':bulan,
        'data':report,
        'Report':True,
    }

    return render(request,'report/update.html',context)    

@login_required
def update(request,tahun,bulan,id):
    dataall = postModel.objects.filter(tahun=tahun,bulan=bulan)
    data = postModel.objects.filter(tahun=tahun,bulan=bulan , id=id)
    dataModels = {
        'tahun':tahun,
        'bulan':bulan,
        'tanggal':data[0].tanggal,
        'body':data[0].body,
    }

    report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    
    dataForm = postForm(request.POST or None , initial=dataModels , instance=data[0])
    if request.method == 'POST':
        if dataForm.is_valid():
            dataForm.save()

            return redirect('report:data',tahun,bulan)

    
    context = {
        'judul':'update data',
        'data':dataall,
        'database':dataForm,
        'tahun':tahun,
        'bulan':bulan,
        'Report':True,
    }
    return render(request, 'report/update.html', context)

@login_required
def delete(request,tahun,bulan,id):
    data = postModel.objects.get(tahun=tahun, bulan=bulan, id=id).delete()
    return redirect('report:data',tahun,bulan)