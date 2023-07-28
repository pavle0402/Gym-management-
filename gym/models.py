from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from itertools import chain




class Member(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    picture = models.ImageField(upload_to="images/", null=True)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(blank=False)
    address = models.CharField(max_length=255, blank=True)
    discount = models.BooleanField(default=False, blank=False)
    training = models.IntegerField(blank=False, 
                                    validators=[
                                        MinValueValidator(0),
                                        MaxValueValidator(100)
                                        ]
                                        )
    registered_on = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.name} {self.last_name}"
    

class SkillChoices(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Trainer(models.Model):

    clients = models.ManyToManyField(Member, related_name='trainers')
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    picture = models.ImageField(upload_to="images/", null=True)
    birthdate = models.DateField(blank=False)
    skills = models.ManyToManyField(SkillChoices)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=255, blank=True)
    registered_on = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.name} {self.last_name}"