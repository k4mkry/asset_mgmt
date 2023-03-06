from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.


class Asset(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    purchase_date = models.DateField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    image = models.FileField(
        upload_to='images/', default='images/asset.jpeg')
    STATUS = (
        ('available', 'Available'),
        ('in use', 'In Use'),
        ('in repair', 'In Repair'),
        ('deleted', 'Deleted')
    )
    status = models.CharField(
        max_length=20, choices=STATUS, blank=True)

    @mark_safe
    def img_preview(self):
        return f'<img src = "{self.image.url}" width = "60"/>'

    def __str__(self) -> str:
        return self.name
