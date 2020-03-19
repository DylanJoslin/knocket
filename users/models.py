from django.db import models
from django import forms
from django.contrib.auth.models import User
from PIL import Image

# UserProfile extends Django's defualt User and adds
# additional properties to the student.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    # Add additional school choices in the future by
    # adding to this list. They will auto populate in
    # the register form.
    SCHOOL_CHOICES = [
        ('Amiskwaciy Academy', 'Amiskwaciy Academy'),
        ('NAIT', 'NAIT')
    ]

    # Access level grants certain permissions:
    #   Pending Approval => No permissions. Can not view video content. Needs Teacher/Admin approval beforee video upload is possible
    #   Student => Log in, submit video for approval, view video  content
    #   Teacher => ~Student, approve video to appear to other students, approve student & teacher account registration
    #   Elder => Log in, submit video for approval in elder teachings section, view video content
    #   Admin => Superuser. Approve Elder teaching videos
    ACCESS_LEVEL = [
        ('pending', 'Pending Approval'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('elder', 'Elder'),
        ('admin', 'Administrator'),
    ]

    access = models.CharField(
        max_length = 10,
        choices = ACCESS_LEVEL,
        default = 'pending'
    )

    school = models.CharField(
        max_length = 100,
        choices = SCHOOL_CHOICES,
        default = 'amiskwaciy'
    )
    
    # If the error relating to user.username appears in your code editor,
    # ignore it. Without this, deleting users in site/admin is impossible.
    # This can be rectified with the pylint plugin.
    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        img.save(self.image.path)

        
    
