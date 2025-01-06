from djongo import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model to be stored as a MongoDB NoSQL collection.
    Extends Django's AbstractUser for username, email, and authentication.
    """
    id = models.ObjectIdField(primary_key=True)  # MongoDB ObjectId
    bio = models.TextField(null=True, blank=True)  # Optional user bio
    profile_image = models.URLField(null=True, blank=True)  # URL to profile image
    created = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated = models.DateTimeField(auto_now=True)  # Automatically update on save

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-created"]