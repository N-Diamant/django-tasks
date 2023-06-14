from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        email=self.normalize_email(email) # to turn the given string to a valid email
        user=self.model(
            email=email, #the email after normalizing
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields): #super users are users that can have admin permissions

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("super user has to have is_staff being true")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser has to have is_superuser being true")


        return self.create_user(email=email,password=password,**extra_fields)

class user(AbstractUser):
    email=models.CharField(max_length=80,unique=True)
    username=models.CharField(max_length=45)
    date_of_birth=models.DateField(null=True)

    objects=customUserManager()
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS=['username']


    def __str__(self) :
        return self.username

