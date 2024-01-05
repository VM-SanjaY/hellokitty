from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Datastore
from .models import Customer

class Datastore_form(forms.ModelForm):
    class Meta:
        model = Datastore
        fields = ("name","desc","datafile")


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ("image",)

        