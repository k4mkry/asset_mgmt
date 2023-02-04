# Generated by Django 4.1.4 on 2023-01-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='image',
            field=models.FileField(default='statis/image/asset.jpeg', upload_to='staic/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
