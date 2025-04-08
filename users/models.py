from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    image = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name=_('image'))
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name=_('email'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('created_at'))

    def full_name(self):
        return self.first_name + ' ' + self.last_name
