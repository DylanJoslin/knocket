from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class VideoPost(models.Model):
    # Content will need to be changed to the video upload. For now I will use text to build the page.
    school = models.CharField(max_length=20)
    content = models.TextField()
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # When referencing a post instance, it will return the name as a string
    def __str__(self):
        return self.title

    # Not entirely sure how this works, but it returns the url?
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})