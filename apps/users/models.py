import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    username = models.CharField(verbose_name=_('Username'), max_length=355)
    firstname = models.CharField(verbose_name=_('First Name'), max_length=50)
    lastname = models.CharField(verbose_name=_('Last Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email Address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self): # Define string representation of the model/class
        return self.username
        
    @property
    def get_full_name(self):
        return f'{self.firstname.title()} {self.lastname.title()}'
        
    def get_short_name(self):
        return self.username
