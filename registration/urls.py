from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate, ProfileResume, CreditCardsView, CreditCardDelete, CreditCardCreate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('resume/', ProfileResume.as_view(), name='resume'),
    path('payment-Methods/', CreditCardsView.as_view(), name='paymentMethods'),
    path('payment-Methods/delete/<int:pk>/', CreditCardDelete.as_view(), name='creditcarddelete'),
    path('payment-Methods/create/', CreditCardCreate.as_view(), name='creditcardcreate'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),
]