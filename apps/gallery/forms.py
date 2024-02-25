from django import forms

from apps.gallery.models import Photography

class PhotographyForm(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published',]
        labels = {
            'name':'Nome',
            'subtitle':'Legenda',
            'category':'Categoria',
            'description':'Descrição',
            'address':'Foto',
            'release_date':'Data de Publicação'        
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'address': forms.FileInput(attrs={'class':'form-control'}),
            'release_date': forms.DateInput(
                format = '%d/%m/%Y',
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'user': forms.Select(attrs={'class':'form-control'})
        }