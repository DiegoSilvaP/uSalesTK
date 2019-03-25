from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Para acceder a los tipos de widgets de un form
from django import forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, EmailForm
from shopping_basket.models import Shopping_basketItem

from wish_list.models import Wish_listItem

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    # Para modificar en tiempo de ejecucion el 
    # enlace y verificar que un usuario se ha registrado 
    # correctamente, hay que redefinir el metodo get_success_url
    def get_success_url(self):
        return  reverse_lazy('login') + '?register'

    # Para sobreescribir los widgets en tiempo de ejecucion
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificacion en tiempo de ejecucion
        form.fields['username'].widget = forms.TextInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Nombre de Usuario'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Dirección de correo'})
        form.fields['password1'].widget =forms.PasswordInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Contraseña'})
        form.fields['password2'].widget =forms.PasswordInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Confirma la contraseña'})
         
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Recuperar el objeto que se va editar
    def get_object(self):
        profile, created = Profile.objects.get_or_create (user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    # Recuperar el objeto que se va editar
    def get_object(self):
        return self.request.user

    # Para sobreescribir los widgets en tiempo de ejecucion
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificacion en tiempo de ejecucion
        form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'form-control mb-2', 'placeholder' : 'Email'})
        return form