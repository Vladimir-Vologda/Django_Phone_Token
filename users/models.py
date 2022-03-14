from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager


def photo_dir(instance, filename):
    #   Функция, при которой сохранение файлов будет
    #   производиться в отдельную папку для каждого пользователя,
    #   папка создаётся по его 'name'
    return f'users/{instance.name}/{filename}'


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(_('Phone number'), unique=True, db_index=True)
    name = models.CharField(_('Username'), unique=True, db_index=True, max_length=50)
    first_name = models.CharField(_('Name'), max_length=50, blank=True)
    last_name = models.CharField(_('Surname'), max_length=50, blank=True)
    photo = models.ImageField(_('Image'), upload_to=photo_dir, default='default/users_default.jpg')
    birthday = models.DateField(_('Birthday'), default='2001-01-01')
    registration_date = models.DateField(_('Registration date'), auto_now_add=True)
    verified_code = models.CharField(_('Verification code'), max_length=5)
    is_active = models.BooleanField(_('Status active'), default=True)
    is_staff = models.BooleanField(_('Status admin'), default=False)
    is_superuser = models.BooleanField(_('Status superuser'), default=False)
    is_verified = models.BooleanField(_('Status verified'), default=False)
    slug = models.SlugField(_('URL-address'), unique=True, db_index=True)

    #   Пользовательский менеджер
    objects = CustomUserManager()

    #   Обязательное поле, по которому пользователь будет входить в систему
    USERNAME_FIELD = 'phone'
    #   Дополнительные обязательные поля,
    #   которые вводятся при регистрации
    REQUIRED_FIELDS = ('name',)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.name} ({self.phone})'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        #   Функция автоматического создания slug,
        #   еси оно ещё не создано
        if not self.pk:
            self.slug = slugify(self.name)
        return super(CustomUserModel, self).save(**kwargs)

    @property
    def get_full_name(self):
        #   Функция представления полного имени
        return f'{self.first_name} {self.last_name}'
