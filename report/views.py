from django.shortcuts import render,redirect
from .forms import postForm
from .models import postModel
from django.contrib.auth.decorators import login_required
from models.db import report
from django import template
from bson.objectid import ObjectId
from datetime import datetime
from helpers.enumDate import monthAsNumber

register = template.Library()

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
    # print('masuk')
    # report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    getRecord = report.find({ 'tahun': tahun, 'bulan': bulan }).sort('tanggal', 1)

    
    context = {
        'judul':'report',
        'data':getRecord,
        'bulan':bulan,
        'tahun':tahun,
        'Report':True,
    }

    return render(request, 'report/report.html', context)

@login_required
def datatambah(request,tahun,bulan):
    # Report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    getReport = report.find({ 'tahun': tahun, 'bulan': bulan })
    # for data in getReport :
    #     print(data)
    

    data = {
        'tahun':tahun,
        'bulan':bulan,
        'tanggal': datetime.now().strftime('%d'),
        'body':'',    
        'Report':True,
    }

    # print(request.POST)

    post = postForm(request.POST or None,initial=data)
    if request.method == 'POST':
        tahun = request.POST['tahun']
        bulan= request.POST['bulan']
        tanggal = request.POST['tanggal']
        body = request.POST['body']

        report.insert_one({
            'tahun': tahun,
            'bulan' : bulan,
            'tanggal': tanggal,
            'body': body
        })
        
        context = {
            'judul':'report',
            'data':getReport,
            'tahun':tahun,
            'bulan':bulan,
            'post':post,
            'Report':True,
        }
        
        return render(request, 'report/report.html', context)

    context = {
        'judul':'report',
        'data':getReport,
        'tahun':tahun,
        'bulan':bulan,
        'post':post,
        'Report':True,
    }
    
    return render(request, 'report/create.html', context)

@login_required
def viewupdate(request,tahun,bulan, slug):
    print('masuk')
    print(slug)
    getReport = report.find({ 'tahun': tahun, 'bulan': bulan })
    
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
        'data':getReport,
        'Report':True,
    }

    return render(request,'report/update.html',context)    

@login_required
def update(request,tahun,bulan,slug):
    print(slug)
    getReport = report.find({  })
    dataall = postModel.objects.filter(tahun=tahun,bulan=bulan)
    data = postModel.objects.filter(tahun=tahun,bulan=bulan , id=id)
    dataModels = {
        'tahun':tahun,
        'bulan':bulan,
        'tanggal':data[0].tanggal,
        'body':data[0].body,
    }

    # report = postModel.objects.filter(tahun=tahun,bulan=bulan)
    
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
def delete(request,tahun,bulan,slug):
    
    report.delete_one({ '_id': ObjectId(slug)})

    return redirect('report:data',tahun,bulan)