from django import forms
from .models import postModel

class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = [
            'semester',
            'matakuliah',
            'Pertemuan',
            'Fle_soal',
            'File_tugas',
        ]

        widgets= {

            'semester':forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'matakuliah':forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'Pertemuan':forms.Select(
                    attrs = {
                        'class':'form-control',
                        
                    }
                ),
            'File_tugas':forms.FileInput(
                    attrs = {
                        'class':'form-control-file',
                    }
                ),
            'Fle_soal':forms.FileInput(
                    attrs = {
                        'class':'form-control-file',
                    }
                ),
        }