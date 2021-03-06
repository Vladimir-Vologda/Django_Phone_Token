from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import CustomUserModel
from users.sendler import send_code


UserModel = get_user_model()


class CustomUserRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = CustomUserModel
        fields = (
            'phone',
            'name',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords don't match"))

        return password2

    def save(self, commit=True):
        user = super(CustomUserRegistrationForm, self).save(commit=False)
        user.verified_code = send_code(self.data.get('phone'))
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class CustomUserChangeFormInAdmin(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUserModel
        fields = (
            'phone', 'name', 'first_name', 'last_name', 'photo',
            'birthday', 'verified_code', 'is_active', 'is_staff', 'is_superuser', 'is_verified', 'slug',
        )


class UserVerificationForm(forms.ModelForm):

    class Meta:
        model = CustomUserModel
        fields = (
            'phone',
            'verified_code',
        )


class CustomAuthUserForm(AuthenticationForm):

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "unverified": _("This account is not verified."),
    }

    def confirm_login_allowed(self, user):

        if not user.is_verified:
            raise ValidationError(
                self.error_messages["unverified"],
                code="unverified",
            )
