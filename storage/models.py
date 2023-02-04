from django.db import models

# Create your models here.


class Asset(models.Model):
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200, blank=True)
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
        max_length=20, choices=STATUS, default='available', blank=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    assets = models.ManyToManyField(Asset, related_name='employees')
