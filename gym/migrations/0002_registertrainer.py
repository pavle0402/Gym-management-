# Generated by Django 4.1.4 on 2023-07-19 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('skills', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.registeruser')),
            ],
        ),
    ]
