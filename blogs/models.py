from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class PostManager(models.Manager):
    def published(self, *args, **kwargs):
        return self.get_queryset().filter(status='published')

    def draft(self, *args, **kwargs):
        return self.get_queryset().filter(status='draft')

    def popular(self, *args, **kwargs):
        return self.published().order_by('-read_count')


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


class Author(Base):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    email = models.EmailField()
    bio = models.TextField('Short bio', blank=True)
    avatar = models.ImageField(upload_to='authors/', blank=True, null=True)

    class Meta:
        ordering = ['full_name', ]

    def __str__(self):
        return self.full_name


class Catagory(Base):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'
        get_latest_by = ['-created_at', '-updated_at', ]
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blogs:catagory-detail', args=[self.slug, ])

    def post_count(self):
        return self.posts.published().count()


class Tag(Base):
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        get_latest_by = ['-created_at', '-updated_at', ]
        ordering = ['title', ]

    def __str__(self):
        return self.title


class Post(Base):
    POST_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ForeignKey(
        Author,
        related_name='posts',
        null=True, on_delete=models.SET_NULL
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
    read_count = models.PositiveIntegerField(default=1)

    # Managers
    objects = PostManager()

    class Meta:
        ordering = ['-created_at', '-updated_at', 'title', ]
        get_latest_by = ['-created_at', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blogs:post-detail', args=[str(self.pk), self.slug])

    def update_read_count(self):
        self.read_count += 1
        self.save()


class Comment(Base):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.TextField('Comment')
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-post', '-created_at', ]
        get_latest_by = ['-created_at', ]

    def __str__(self):
        return '{} comment on {}'.format(self.full_name, self.post)
