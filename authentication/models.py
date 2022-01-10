import uuid

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, Permission, Group
)
from django.utils.translation import gettext_lazy as _

from authentication.managers import CustomUserManager


class SearchPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = _('Permission')
        verbose_name_plural = _('Permissions')


class SearchGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name=_('e-mail address'), unique=True,
        error_messages={'unique': _('this e-mail already exists')}
    )
    cpf = models.CharField(
        verbose_name=_('CPF'), unique=True,
        error_messages={'unique': _('this CPF already exists')}
    )
    phone = models.CharField(
        verbose_name=_('phone'), unique=True, null=True, blank=True,
        error_messages={'unique': _('this phone number already exists')}
    )
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    is_active = models.BooleanField(_('is active'), default=True)
    is_superuser = models.BooleanField(_('is superuser'), default=False)
    is_staff = models.BooleanField(
        verbose_name=_('is staff'), default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_trusty = models.BooleanField(
        _('trusty'), default=False,
        help_text=_('designates whether this user has confirmed his account.')
    )
    groups = models.ManyToManyField(
        'SearchGroups',
        verbose_name=_('groups'),
        related_name='user_set',
        related_query_name='user',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'SearchPermission',
        verbose_name=_('permissions'),
        related_name='user_set',
        related_query_name='user',
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'first_name', 'last_name']
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self) -> str:
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs) -> None:
        send_mail(subject, message, from_email, [self.email])
