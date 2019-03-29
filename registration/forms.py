from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Plastic_money

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo y debe ser un correo válido')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        

# Metodo para limpiar o validar el email
    def clean_email(self):
        # Recuperamos el email que se ha enviado en el formulario
        email = self.cleaned_data.get('email')
        # comprobar si existen en la bd uno o mas emails con la misma direccion
         # Filter a diferencia de get, devuelve un queryset o una lista vacia si no hay ningun elemento
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado, prueba con otro.')
       
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','phone', 'address']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'phone': forms.TextInput(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Teléfono'}),
            'address': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Dirección'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo y debe ser un correo válido')

    class Meta:
        model = User
        fields = ['email']

    # Metodo para limpiar o validar el email
    def clean_email(self):
        # Recuperamos el email que se ha enviado en el formulario
        email = self.cleaned_data.get('email')
        # Comprobamos si se ha cambiado el campo email
        if 'email' in self.changed_data:
            # comprobar si existen en la bd uno o mas emails con la misma direccion
            # Filter a diferencia de get, devuelve un queryset o una lista vacia si no hay ningun elemento
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya está registrado, prueba con otro.')
        return email

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = Plastic_money
        fields = ['entity', 'card_number','exp_month', 'exp_year', 'owner_profile', 'owner','cvv']
        widgets = {
            'entity': forms.Select(attrs={'class':'form-control mt-3'}),
            # 'type_card': forms.Select(attrs={'class':'form-control mt-3'}),
            'card_number': forms.TextInput(attrs={'class':'form-control mt-3'}),
            'exp_month': forms.Select(attrs={'class':'form-control mt-3'}),
            'exp_year': forms.Select(attrs={'class':'form-control mt-3'}),
            'owner_profile': forms.TextInput(attrs={'class':'form-control mt-3'}),
            'owner': forms.TextInput(attrs={'class':'form-control mt-3'}),
            'cvv': forms.TextInput(attrs={'class':'form-control mt-3'}),
        }