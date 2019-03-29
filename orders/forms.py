from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Orders
        fields = [ 'payment_method', 'payment_status']
        widgets = {
            'payment_method': forms.Select(attrs={'class':'form-control mb-3'}),
            'payment_status': forms.Select(attrs={'class':'form-control mb-3'}),
        }