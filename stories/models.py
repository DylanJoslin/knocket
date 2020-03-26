from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name
# class School(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'school'
#         verbose_name_plural = 'schools'

#     def __str__(self):
#         return self.name


class VideoPost(models.Model):
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # school = models.ForeignKey('School', on_delete=models.CASCADE)
    SCHOOL_CHOICES = [
        ('Amiskwaciy-Academy', 'Amiskwaciy Academy'),
        ('NAIT', 'NAIT'),
    ]

    CATEGORY_CHOICES = [
        ('Emotional', 'Emotional'),
        ('Mental', 'Mental'),
        ('Physical', 'Physical'),
        ('Spiritual', 'Spiritual')
    ]
    school = models.CharField(
        max_length = 100,
        choices = SCHOOL_CHOICES,
        default = 'NOT SET'
    )

    category = models.CharField(
        max_length = 100,
        choices = CATEGORY_CHOICES,
        default = 'NOT SET'
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    approve = models.BooleanField(default = False)

    def _get_unique_slug(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(VideoPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title