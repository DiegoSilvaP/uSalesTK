from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication
        fields = ['seller', 'product', 'category', 'description', 'stock', 'price', 'picture']
        widgets = {
            'seller': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vendedor'}),
            'product': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Producto'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'picture': forms.FileInput(attrs={'class':'form-control'}),
        }
        