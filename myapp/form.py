from django import forms
from .models import todo

class Listform(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['head','content']