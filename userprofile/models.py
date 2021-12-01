from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from utils.constants import GENDER_CHOICE


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=30, unique=True)
    email = models.EmailField(
        db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0.00
    
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='address',
        on_delete=models.CASCADE,
    )
    created_by_admin_user = models.ForeignKey(
        User,
        related_name='created_by_admin_user_profile',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_img = models.ImageField(_("Profile Image"))
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=256)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICE, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}' '{self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name}' '{self.last_name}"
        

    class Meta:
        verbose_name_plural = _('Users Profile')
