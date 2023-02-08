from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RiceItemForm(forms.ModelForm):
    class Meta:
        model = RiceItem
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs = {'class' : 'form-control'}),
            'price': forms.NumberInput(attrs = {'class' : 'form-control'}),
            'loanPrice': forms.NumberInput(attrs = {'class' : 'form-control'}),
            'quantity': forms.NumberInput(attrs = {'class' : 'form-control'}),
            'image': forms.FileInput(attrs = {'class' : 'form-control-file'}),
        }

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = 'orderStatus', 'shippingStatus'

        widgets = {
            'orderStatus': forms.Select(attrs = {'class': 'form-select form-select-md mb-3'}),
            'shippingStatus': forms.Select(attrs = {'class': 'form-select form-select-md mb-3'})
        }

class LendingForm(forms.ModelForm):
    class Meta:
        model = LendingStat
        fields = 'amount_paid', 

        widgets = {
            'amount_paid': forms.NumberInput(attrs = {'class': 'form-control mb-6'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = 'barangay', 'street', 'ContactNum', 'loan', 'customer_id', 'method'

        widgets = {
            'barangay': forms.Select(attrs = {'class': 'input-select'}),
            'street': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Bldg/Drive/House No./Street'}), 
            'ContactNum': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': '09XXXXXXXXX'}), 
            'loan': forms.CheckboxInput(attrs = {'class': 'input-checkbox', 'id' : 'shiping-address', 'onclick': 'myFunction()'}), 
            'customer_id':  forms.FileInput(attrs = {'class' : 'form-control-file', 'id' : 'customer-id'}),
            'method': forms.Select(attrs = {'class': 'input-select'})
        }