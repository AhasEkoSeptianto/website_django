from django.db import models
from django.utils.text import slugify

# Create your models here.
class postModel(models.Model):
    namaaplikasi        = models.CharField(max_length=200)
    gambaraplikasi      = models.ImageField(upload_to='static/media')
    contentaplikasi     = models.TextField()
    penjelasan          = models.TextField(blank=True)
    fileaplikasi        = models.FileField(upload_to='static/media/field',blank=True)
    slug                = models.SlugField(blank=True,editable=False)


    def save(self):
        self.slug = slugify(self.namaaplikasi)
        super(postModel,self).save()
    
    def __str__(self):
        return "{}.{}".format(self.id , self.namaaplikasi)
 