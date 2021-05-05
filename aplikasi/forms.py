from django import forms
from .models import postModel


class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = [
            'namaaplikasi',
            'gambaraplikasi',
            'contentaplikasi',
            'penjelasan',
            'fileaplikasi'
        ]
        widgets = {
            'namaaplikasi' : forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'gambaraplikasi':forms.FileInput(
                attrs={
                    'class':'form-control-file',
                }
            ),

            'contentaplikasi' : forms.Textarea(
                attrs={
                    'class':'form-control',
                }
            ),

            'penjelasan' : forms.Textarea(
                attrs={
                    'class':'form-control',
                }
            ),

            'fileaplikasi':forms.FileInput(
                attrs={
                    'class':'form-control-file',
                }
            ),

        }