from django.db import models


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
    story = models.TextField('Background story', blank=True)
    who = models.TextField('Who we are', blank=True)
    what = models.TextField('What we do', blank=True)
    team_description = models.TextField('Team description', blank=True)
    service_description = models.TextField('Service description', blank=True)
    contact_description = models.TextField('Contact description', blank=True)
    address = models.TextField('Compay address', blank=True)
    phone1 = models.CharField(max_length=30, blank=True)
    phone2 = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    keywords = models.TextField(
        blank=True,
        help_text='Comma separated keywords. Ex: abl, electrical, consulting, '
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'

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
    icon = models.TextField()
    link_title = models.CharField(max_length=60)
    link_url = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Staff(Base):
    """
    Models team staff
    """
    name = models.CharField('Full name', max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    facebook = models.URLField('Facebook link', blank=True)
    twitter = models.URLField('Twitter link', blank=True)
    Linkedin = models.URLField('Linkedin link', blank=True)
    picture = models.ImageField(
        upload_to='staff/',
        blank=True, null=True,
        help_text='Recommended picture size is 400x499 pixels'
    )

    def __str__(self):
        return self.name


class Service(Base):
    """
    Models provided services
    """
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField(default=False)

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
    description = models.TextField('Testimonial')
    quote = models.TextField(max_length=255)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', '-rating', ]

    def __str__(self):
        return self.title

    def get_stars(self, *args, **kwargs):
        i = 1
        stars = []
        while i <= 5:
            if i <= self.rating:
                stars.append('*')
            else:
                stars.append('')
            i += 1

        return stars


class Client(Base):
    """
    Models a Client
    """
    title = models.CharField('Client name', max_length=255)
    logo = models.ImageField(upload_to='clients/logo/')
    link = models.URLField('Client webiste link', blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', ]

    def __str__(self):
        return self.title


class Subscriber(Base):
    """
    Models a subscriber
    """
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Email subscriber'
        verbose_name_plural = 'Email subscribers'
        ordering = ['-created_at', 'email', ]

    def __str__(self):
        return self.email
