from django import forms
from django.forms import widgets


class NoteForm(forms.Form):
    author = forms.CharField(max_length=200, required=True, label="Название")
    email = forms.EmailField(max_length=200, required=True, label="Автор")
    text = forms.CharField(max_length=2000, required=True, label="Текст", widget=widgets.Textarea(attrs={"rows": 5, "cols":50}))