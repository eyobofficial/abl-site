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
