from django.contrib import admin
from .models import postModel

class PostAdmin(admin.ModelAdmin):	
	readonly_fields = ['slug',]

# Register your models here.
admin.site.register(postModel,PostAdmin)