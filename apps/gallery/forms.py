from django import forms

from apps.gallery.models import Photography


class PhotographyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(PhotographyForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        photo = super(PhotographyForm, self).save(commit=False)
        if not photo.pk:  # Verifica se é uma nova instância
            photo.user = self.user  # Associa o usuário ao objeto photo
        if commit:
            photo.save()
        return photo

    class Meta:
        model = Photography
        exclude = ["published", "user"]
        labels = {
            "name": "Nome",
            "subtitle": "Legenda",
            "category": "Categoria",
            "description": "Descrição",
            "address": "Foto",
            "release_date": "Data de Publicação",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "subtitle": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "address": forms.FileInput(attrs={"class": "form-control"}),
            "release_date": forms.DateInput(
                format="%d/%m/%Y", attrs={"type": "date", "class": "form-control"}
            ),
        }
