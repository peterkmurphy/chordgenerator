from django import forms
from django.forms.widgets import Textarea;
from django.forms import ModelForm

class SimpleOrderForm(forms.Form):
    orders = forms.IntegerField(label="Copies", min_value=1);
    hidden_slug = forms.CharField(widget=forms.HiddenInput);
    



