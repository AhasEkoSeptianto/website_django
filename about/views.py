from django.shortcuts import render
from aplikasi.models import postModel

# Create your views here.
def index(request):
    semuaapp = postModel.objects.all()
    context = {
        'myapp':semuaapp,
        'judul':'About',
        'About':True,
    }
    return render(request, 'about/index.html', context)