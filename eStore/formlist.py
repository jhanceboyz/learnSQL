from logging import PlaceHolder
from django.forms.fields import CharField
from django import forms

class searchticketbox(forms.Form):
    searchticket = forms.CharField(PlaceHolder= "Search")