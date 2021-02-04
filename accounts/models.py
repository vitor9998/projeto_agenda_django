from django.db import models
from contatos.models import Contato
from django import forms

class FormContato(forms.ModelForm):
    class Meta:
        model =Contato
        exclude = ('mostrar',)



#odjango faz uma "mágica" e cria um form completo pra gente.
#No exclude eu coloco o que eu quero excluir do form completo.
