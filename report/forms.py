from django import forms
from .models import postModel

class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = [
            'tahun',
            'bulan',
            'tanggal',
            'body'
        ]

        widgets = {

            'tahun':forms.TextInput(
               attrs={
                   'class':'form-control',
                   'readonly':'',
               }
            ),
            
            'bulan':forms.TextInput(
               attrs={
                   'class':'form-control',
                   'readonly':'',
               }
            ),
           
            'tanggal' : forms.TextInput(
               attrs={
                'class':'form-control',
                },
            ),

            'body':forms.Textarea(
               attrs={
                   'class':'form-control',
               }
            )
           
       }