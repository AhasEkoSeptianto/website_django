from django.db import models

# Create your models here.
class postModel(models.Model):
    tahun       = models.CharField(max_length=20)
    bulan       = models.CharField(max_length=20)
    tanggal     = models.CharField(max_length=2)
    body        = models.TextField()

    def __str__(self):
        return "{}.{}".format(self.tanggal, self.bulan)