from django.urls import path

from users.views import CustomRegistrationUser, verification_user

urlpatterns = [
    path('', CustomRegistrationUser.as_view(), name='registration'),
    path('verification/', verification_user, name='verification'),
]
