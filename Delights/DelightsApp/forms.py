from django import forms

from .models import *

class AddPurchase(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'