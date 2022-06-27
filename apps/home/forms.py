from django import forms
from django.forms import ChoiceField, TextInput
from .models import *

parall = (("id_doc", "Код документа"), ("autor", "Автор документа"), ("isbn", "ISBN документа"), ("short_name", "Название документа"))

class SearchForm(forms.Form):
    parametr = forms.ChoiceField(choices = parall, label="", widget=forms.Select(attrs={'class': 'form-select-sm browser-default custom-select mb-2 w-25'}))
    value = forms.CharField(max_length=255, label="", help_text="Введите значение поиска (обратите внимание на регистр букв)", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ml-3'}))

    class Meta:
        widgets = {
            "value": TextInput(attrs={
                'class': 'form-control form-control-sm ml-3',
            })
        }