from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'auth_user_custom'


    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups',  
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_permissions',  
        related_query_name='user'
    )


class blog_category(models.Model):
    category = models.CharField(blank=True, null=True, max_length=255)
    decription = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.category



class post_create(models.Model):
    author = models.CharField(blank=True, null=True, max_length=255)
    category = models.ForeignKey(blog_category, on_delete=models.CASCADE, related_name='Python', default=1 )
    title = models.CharField(max_length=200, null=True, blank=True)
    question = models.CharField(max_length=255)
    code = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(blank=True, null=True, max_length=255)
    full_details = models.TextField(null=True, blank=True)
    image = models.FileField(default="", upload_to="autopost/", null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    slug = models.SlugField(max_length=500, blank=True)


    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:500]  
        super().save(*args, **kwargs)
