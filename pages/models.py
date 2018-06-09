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

