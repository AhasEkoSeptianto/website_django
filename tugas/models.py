from django.db import models
from django.utils.text import slugify

# Create your models here.
class postModel(models.Model):
    semester        = models.CharField(max_length=20)
    matakuliah      = models.CharField(max_length=50)
    pertemuan       = (
                    (1,1),
                    (2,2),
                    (3,3),
                    (4,4),
                    (5,5),
                    (6,6),
                    (7,7),
                    (8,8),
                    (9,9),
                    (10,10),
                    (11,11),
                    (12,12),
                    (13,13),
                    (14,14),
                    (15,15),
                    (16,16),   
                )

    Pertemuan       = models.IntegerField(
                        default=1,
                        choices=pertemuan,
                    )
    File_tugas      = models.FileField(upload_to='',blank=True)
    Fle_soal        = models.FileField(upload_to='',blank=True)
    publish         = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.matakuliah)
        super().save()

    def __str__(self):
        return "no {}.semester {}\t{}\t{}".format(self.id,self.semester, self.matakuliah,self.Pertemuan)