from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Votre nom", max_length=50)
