import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    headline = models.CharField(max_length=255, verbose_name='Headline', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Slug', db_index=True, blank=True)
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified_at = models.DateTimeField(verbose_name='Modified at', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} : {self.headline}'

    def save(self, *args, **kwargs):
        self.modified_at = datetime.datetime.now()
        self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:post-detail', kwargs={
            'year': self.created_at.year,
            'month': self.created_at.month,
            'day': self.created_at.day,
            'slug': self.slug,
        })
