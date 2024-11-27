import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Adversitement(BaseModel):
    image = models.ImageField(upload_to='common/advertisement')
    link = models.URLField()

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name = 'Adverstisement'
        verbose_name_plural = 'Advertisements'

class ContactUs(BaseModel):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(
        max_length=120,
        validators=[
            RegexValidator(
                regex=r'^\+?[1-9]\d{1,14}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ])
    is_contacted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name or self.phone_number
    
    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')
        ordering = ['-is_contacted']


class AboutUs(BaseModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    video = models.FileField(upload_to='common/aboutus/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')