from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_university_student = models.BooleanField(default=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username} Profile"
