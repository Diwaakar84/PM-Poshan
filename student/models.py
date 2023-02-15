from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from school.models import School
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import User

# Create your models here.

# from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


# class StudentManager(BaseUserManager):

#     def create_superuser(self, aadhar, name, password, **other_fields):

#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(aadhar = aadhar, name = name, password = password, **other_fields)

#     def create_user(self, aadhar, name, password, **other_fields):

#         if not aadhar:
#             raise ValueError(_('You must provide an aadhar number'))

#         user = self.model(aadhar = aadhar, name = name,
#                           **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    stud_sex_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    stud_bloodgrp_choices = (
        ('O', 'O'),
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB')
    )

    aadhar = models.CharField(max_length = 12, primary_key = True, unique = True)
    admission_no = models.CharField(max_length = 20, unique = True)
    name = models.TextField()
    sex = models.CharField(max_length = 1, choices = stud_sex_choices)
    bloodgrp = models.CharField(max_length = 2, choices = stud_bloodgrp_choices)
    birthdate = models.DateField()
    parent_guardian = models.TextField()
    stud_class = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits = 5, decimal_places = 2)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2)

    # objects = StudentManager()

    # USERNAME_FIELD = 'aadhar'
    # REQUIRED_FIELDS = ['name']
    # REQUIRED_FIELDS = ['name', 'school', 'sex', 'admission_no', 'birthdate']


