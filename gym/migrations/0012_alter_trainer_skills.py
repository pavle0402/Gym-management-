# Generated by Django 4.2.3 on 2023-07-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_alter_trainer_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='skills',
            field=models.CharField(choices=[('Kickboxing', 'Kickboxing'), ('Boxing', 'Boxing'), ('Mma', 'Mma'), ('Weightlifting', 'Weightlifting'), ('Cardio', 'Cardio'), ('Crossfit', 'Crossfit')], default='Kickboxing', max_length=255),
        ),
    ]
