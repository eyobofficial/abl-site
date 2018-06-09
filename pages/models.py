from django.db import models


class Base(models.Model):
    """
    Abstract Base Model
    """
    created_at = models.DateTimeField(
        'Created Date',
        auto_now_add=True,
        help_text='Record first created date and time'
    )
    updated_at = models.DateTimeField(
        'Last Modified',
        auto_now=True,
        help_text='Record last modified date and time'
    )

    class Meta:
        abstract = True
        get_latest_by = ['-updated_at', ]


class Brand(Base):
    """
    Models the Company Brand
    """
    title = models.CharField('Company title', max_length=100)
    logo = models.ImageField(
        'Company logo', upload_to='brand/logo/',
        blank=True, null=True
    )
    background = models.ImageField(
        'Background Picture',
        blank=True, null=True,
    )
    fevicon = models.ImageField(
        'Fevicon (Title Icon)',
        upload_to='fevicon/',
        null=True, blank=True,
    )
    story = models.TextField('Background story')
    who = models.TextField('Who we are')
    what = models.TextField('What we do')
    service_description = models.TextField('Service description', blank=True)
    contact_description = models.TextField('Contact description', blank=True)
    address = models.TextField('Compay address')
    phone1 = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    keywords = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Slide(Base):
    """
    Models Slides
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Widget(Base):
    """
    Models widgets for home page
    """
    title = models.CharField(max_length=60)
    sub_title = models.TextField(max_length=255)
    icon = models.CharField(max_length=255)
    link_title = models.CharField(max_length=60)
    link_url = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Service(Base):
    """
    Models provided services
    """
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(Base):
    """
    Models client testimonials
    """
    RATING_CHOICE_OPTIONS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    client = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    picture = models.ImageField(
        upload_to='testimonials/clients/',
        blank=True, null=True
    )
    rating = models.PositiveIntegerField(choices=RATING_CHOICE_OPTIONS)
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', '-rating', ]

    def __str__(self):
        return self.title


class Client(Base):
    """
    Models a Client
    """
    title = models.CharField('Client name', max_length=255)
    logo = models.ImageField(upload_to='clients/logo/')
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', ]

    def __str__(self):
        return self.title