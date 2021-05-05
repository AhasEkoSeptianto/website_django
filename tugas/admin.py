from django.contrib import admin
from .models import postModel

class TugasAdmin(admin.ModelAdmin):
    read_only = [
        'publish',
        'update',
        'slug',
    ]

# Register your models here.
admin.site.register(postModel,TugasAdmin)