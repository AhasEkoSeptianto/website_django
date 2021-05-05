from django.shortcuts import render,redirect
from .models import postModel
from .forms import postForm
import os

# Create your views here.
def index(request):

    tugassemua = postModel.objects.all()
    context = {
        'judul':'Tugas',
        'datapkn':tugassemua,
        'Tugas':True,
    }
    return render(request, 'tugas/index.html', context)

# daftar tugas
def daftarTugas(request, semester,matakuliah):
    berdasarkanMatakuliah = postModel.objects.filter(semester=semester,matakuliah=matakuliah)
    sortedmatkul    = berdasarkanMatakuliah.order_by('Pertemuan')

    context = {
        'judul':'Daftar Tugas',
        'matkul':sortedmatkul,
        'matakuliah':matakuliah,
        'Tugas':True,
    }
    return render(request, 'tugas/daftarTugas.html', context)


def create(request,semester,matakuliah):

    initial = {
        'semester':semester,
        'matakuliah':matakuliah,
    }

    myform = postForm(request.POST or None,request.FILES or None, initial=initial)

    if request.method == 'POST':
        if myform.is_valid():
            myform.save()

            return redirect('tugas:daftarTugas',semester,matakuliah)

    context = {
        'judul':'create',
        'formcreate':myform,
        'Tugas':True,
    }

    return render(request,'tugas/create.html',context)


def delete(request,semester,matakuliah,id):

    myFile  = postModel.objects.filter(semester=semester,matakuliah=matakuliah,id=id).delete()

    return redirect('tugas:daftarTugas',semester,matakuliah)

def update(request,semester,matakuliah,id,pertemuan):

    myforms = {
        'semester':semester,
        'matakuliah':matakuliah,
        'Pertemuan': pertemuan
    }

    form = postForm(request.POST or None,request.FILES or None,initial=myforms)

    if request.method == 'POST':
    
        myfiletodel = postModel.objects.get(semester=semester,matakuliah=matakuliah,id=id)
        form = postForm(request.POST,request.FILES)
        if form.is_valid():
            pathFileTugas = '../media/' + str(myfiletodel.File_tugas)
            pathFileSoal = '../media/' + str(myfiletodel.Fle_soal)
            form.save()
            myfiletodel.delete()
            # delete file if exists
            if os.path.exists('urls.py'):
                print("masuk")
                # os.remove(pathFileSoal)

            if os.path.exists(str(pathFileTugas)):
                print("masuk")
                os.remove(pathFileTugas)

            return redirect('tugas:daftarTugas',semester,matakuliah)
    
    context = {
        'judul':'Updata Tugas',
        'dataForm':form,
        'Tugas':True,
    }

    return render(request,'tugas/update.html',context)