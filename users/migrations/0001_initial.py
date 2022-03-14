# Generated by Django 4.0.3 on 2022-03-14 08:58

from django.db import migrations, models
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, unique=True, verbose_name='Phone number')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Surname')),
                ('photo', models.ImageField(default='default/users_default.jpg', upload_to=users.models.photo_dir, verbose_name='Image')),
                ('birthday', models.DateField(default='2001-01-01', verbose_name='Birthday')),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='Registration date')),
                ('verified_code', models.CharField(max_length=5, verbose_name='Verification code')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Status admin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Status superuser')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Status verified')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
