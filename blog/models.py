from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    body_en = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class About(models.Model):
    title_uz = models.CharField(max_length=200, default="Men haqimda")
    title_en = models.CharField(max_length=200, default="About Me")

    body_uz = models.TextField(
        default="Men Abdukarim Qarshiyev, dasturlash va texnologiyaga qiziqqan yosh dasturchiman.")
    body_en = models.TextField(
        default="I'm Abdukarim Qarshiyev, a young developer passionate about technology and software engineering.")

    telegram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    leetcode = models.URLField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Section"
