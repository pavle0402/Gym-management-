# Generated by Django 4.1.4 on 2023-07-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_member_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
