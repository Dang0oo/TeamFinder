from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about = models.TextField(blank=True)
    mobile = models.CharField(max_length=17, blank=True)
    git_profile = models.URLField(blank=True)