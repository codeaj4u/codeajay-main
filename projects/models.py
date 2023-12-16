from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='project_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='project_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    ratings = models.IntegerField(default=0, blank=True, null=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title if self.title else "Untitled Project"

    def get_absolute_url(self):
        return f"/projects/{self.slug}"
