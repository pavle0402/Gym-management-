# Generated by Django 4.1.4 on 2023-07-19 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_registeruser_trainer_remove_registertrainer_clients_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisterUser',
            new_name='Member',
        ),
        migrations.RenameModel(
            old_name='RegisterTrainer',
            new_name='Trainer',
        ),
    ]
