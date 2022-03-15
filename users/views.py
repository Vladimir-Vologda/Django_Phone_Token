from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from users.forms import CustomUserRegistrationForm, UserVerificationForm
from users.models import CustomUserModel

User = get_user_model()


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

        return HttpResponseRedirect('/users')

    context = {
        'form': form,
    }

    return render(request, 'users/verification_user.html', context)
