from django.urls import path

from users.views import CustomRegistrationUser, verification_user, HomeUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path('', CustomRegistrationUser.as_view(), name='registration'),
    path('verification/', verification_user, name='verification'),
    path('home/', HomeUserView.as_view(), name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
