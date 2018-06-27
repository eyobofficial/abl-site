from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class CustomUser(AbstractUser):
    pass


class Base(models.Model):
    """
    Abstract Base Model
    """
    created_at = models.DateTimeField(
        'Created Date',
        null=True, blank=True,
        auto_now_add=True,
        help_text='Record first created date and time'
    )
    updated_at = models.DateTimeField(
        'Last Modified',
        null=True, blank=True,
        auto_now=True,
        help_text='Record last modified date and time'
    )

    class Meta:
        abstract = True
        get_latest_by = ['-updated_at', ]


class Catagory(Base):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'
        get_latest_by = ['-updated_at', ]
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blogs:post-detail', args=[self.slug, ])


class Tag(Base):
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        get_latest_by = ['-updated_at', ]
        ordering = ['title', ]

    def __str__(self):
        return self.title


class Post(Base):
    POST_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    catagory = models.ForeignKey(
        Catagory,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    summary = models.TextField('Short summary', blank=True)
    content = models.TextField('Post')
    picture = models.ImageField(upload_to='posts/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='posts', blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=POST_STATUS_CHOICES,
        default='draft',
    )
    tags = models.ManyToManyField(
        Tag, blank=True,
        related_name='posts',
    )
    open_for_comment = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated_at', ]
        get_latest_by = ['-updated_at', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blogs:post-detail', args=[str(self.pk), self.slug])
