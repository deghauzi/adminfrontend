from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from utils.constants import GENDER_CHOICE


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=30, unique=True)
    email = models.EmailField(
        db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f"{self.email}"
    
    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0.00
    @property
    def is_staff(self):
        return self.is_admin
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='address',
        on_delete=models.CASCADE,
    )
    created_by_admin_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_by_admin_user_profile',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    street_address = models.TextField()
    city = models.CharField(max_length=256)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_img = models.ImageField(_("Profile Image"))
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=25)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICE)
    birth_date = models.DateField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        

    class Meta:
        verbose_name_plural = _('Users Profile')

    def save(self, *args, **kwargs):
        for field_name in ["first_name", "last_name"]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(UserProfile, self).save(*args, **kwargs)
