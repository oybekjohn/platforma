from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + self.last_name
