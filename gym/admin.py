from django.contrib import admin
from .models import Member, Trainer, SkillChoices

admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(SkillChoices)

