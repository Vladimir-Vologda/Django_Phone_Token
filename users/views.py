from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, RedirectView

from users.forms import CustomUserRegistrationForm, UserVerificationForm, CustomAuthUserForm
from users.models import CustomUserModel

User = get_user_model()


class HomeUserView(ListView):
    model = CustomUserModel
    template_name = 'users/home_user.html'
    context_object_name = 'home-list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeUserView, self).get_context_data(**kwargs)
        context['title'] = _('Home')
        return context


class CustomRegistrationUser(CreateView):
    form_class = CustomUserRegistrationForm
    model = CustomUserModel
    template_name = 'users/registration_user.html'
    success_url = reverse_lazy('verification')

    def get_context_data(self, **kwargs):
        context = super(CustomRegistrationUser, self).get_context_data(**kwargs)
        context['title'] = _('Registration')
        return context


def verification_user(request):
    form = UserVerificationForm

    if request.method == 'POST':
        phone = request.POST.get('phone')
        code = request.POST.get('verified_code')
        phone_db = CustomUserModel.objects.get(phone=phone)

        if code == phone_db.verified_code:
            phone_db.is_verified = True
            phone_db.save()
            return redirect('login')

        else:
            return redirect('verification')

    context = {
        'form': form,
    }

    return render(request, 'users/verification_user.html', context)


class LoginUserView(LoginView):
    form_class = CustomAuthUserForm
    template_name = 'users/authentication_user.html'

    def get_context_data(self, **kwargs):
        context = super(LoginUserView, self).get_context_data(**kwargs)
        context['title'] = _('Authenticated')
        return context


class LogoutUserView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUserView, self).get(request, *args, **kwargs)
