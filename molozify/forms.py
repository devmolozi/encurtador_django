from django import forms
from .models import Link


class FormLink(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        widgets = {
            'link_redirect': forms.TextInput(attrs={'placeholder': 'Seu link aqui'}),
            'link_encurtado': forms.TextInput(attrs={'placeholder': 'Palavra chave'}),
        }

    def clean_link_encurtado(self):
        link_encurtado = self.cleaned_data.get('link_encurtado')
        if ' ' in link_encurtado:
            raise forms.ValidationError("A palavra chave não pode conter espaços.")
        return link_encurtado