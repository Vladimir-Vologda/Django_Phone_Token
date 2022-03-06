from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, phone, name, password=None, **extra_fields):
        """
       Create and save user
        """
        if not phone:
            raise ValueError(_('The Phone number must be'))

        if not name:
            raise ValueError(_('The Name must be'))

        user = self.model(
            phone=phone,
            name=name,
            **extra_fields,
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, name, password=None, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        user = self.create_user(
            phone=phone,
            name=name,
            password=password,
            **extra_fields,
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
