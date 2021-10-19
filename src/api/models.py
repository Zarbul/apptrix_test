from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from src.api.services import get_path_upload_avatar, validate_size_image


class AuthUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=150, unique=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image],
        default='media/apptrix.jpg'
    )

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'gender']
    USERNAME_FIELD = 'email'

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f'{self.email}'

    def save(self, *args, **kwargs):
        self.username = self.email
        self.add_watermark()
        return super(AuthUser, self).save(*args, **kwargs)

    def add_watermark(self):
        pos = (0, 0)
        photo = Image.open(self.avatar)
        watermark = Image.open('media/apptrix.jpg')
        photo.paste(watermark, pos)
        temp = BytesIO()
        photo.save(temp, 'JPEG')
        temp.seek(0)
        self.avatar.save(self.avatar, ContentFile(temp.read()), save=False)
        temp.close()
