from django.db import models
from django.template.defaultfilters import title


class Posts(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title