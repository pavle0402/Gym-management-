# Generated by Django 4.1.4 on 2023-07-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_trainer_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
