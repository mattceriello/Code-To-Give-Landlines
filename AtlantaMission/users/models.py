from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from PIL import Image

# Create your models here.
## We are inheriting the User model and creating a new model Profile which includes profile pictures and other necessary fields.
## There is one to one relationship between user and profile.

## Anytime you make changes to the database you should migrate

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    propic = models.ImageField(default = 'user.png', upload_to= 'profile_pics')

    def __str__(self):
        return f' {self.user.username} Profile'

## We are commenting the below code as it is not necessary for the S3 storage.
## If we want to do the same in S3, we can use AWS lambda function to resize the images.

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.propic.path)

    #     if img.height > 370 or img.width > 370:
    #         output_size = (370, 370)
    #         img.thumbnail(output_size)
    #         img.save(self.propic.path)