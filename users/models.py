import typing

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

from users.validators import validate_name_field


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: typing.Optional[str] = None) -> AbstractBaseUser:
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: typing.Optional[str] = None) -> AbstractBaseUser:
        """
        Creates and saves a Superuser with the given email and password.
        """
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Person(AbstractBaseUser):
    email = models.EmailField(
        max_length=60,
        unique=True,
    )
    first_name = models.CharField(max_length=30, validators=[validate_name_field], blank=True)
    last_name = models.CharField(max_length=30, validators=[validate_name_field], blank=True)
    phone = PhoneNumberField(blank=True, region="RU")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> typing.Text:
        return str(self.email)

    def get_full_name(self) -> typing.Text:
        return f"{self.last_name} {self.first_name}"

    def has_perm(self, perm: typing.Any, obj: typing.Optional[AbstractBaseUser] = None) -> models.BooleanField:
        """Does the user have a specific permission?"""
        return self.is_admin

    def has_module_perms(self, app_label: typing.Any) -> typing.Literal[True]:
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self) -> models.BooleanField:
        """Is the user a member of staff?"""
        return self.is_admin
