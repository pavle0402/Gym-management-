from django import forms 
from .models import Member, Trainer, SkillChoices
from django.utils.safestring import mark_safe



class RegisterMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'last_name','trainer', 'picture', 'email', 'phone_number', 'address', 'birthdate','training' ,'discount')
        labels = {
            'name':'Name',
            'last_name':'Last name',
            'picture':'Picture',
            'trainer':'Mentor',
            'email':'Email',
            'phone_number':'Phone',
            'address':'Address',
            'birthdate':'Date of birth',
            'training':'Sessions',
            'discount':'Student discount',
        }
        help_text = {
            'training':'Set the amount of session this member has purchased when registering.'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-class', 'placeholder':"Enter member's name."}),
            'last_name': forms.TextInput(attrs={'class':'form-class', 'placeholder':"Enter member's last name."}),
            'email': forms.EmailInput(attrs={'class':'form-class', 'placeholder':"Enter member's email."}),
            'address': forms.TextInput(attrs={'class':'form-class', 'placeholder':"Enter member's address."}),
            'birthdate': forms.DateInput(attrs={'class':'form-class', 'type':'date', 'placeholder':"Enter member's birthdate."}),
            'discount': forms.CheckboxInput(attrs={'class':'form-class'}),

        }




class RegisterTrainerForm(forms.ModelForm):


    class Meta:
        model = Trainer
        fields = ('name', 'last_name','picture', 'skills', 'birthdate', 'phone_number', 'email', 'address')

        labels = {
            'name':'Name',
            'last_name':'Last name',
            'clients':'Clients',
            'picture':'Picture',
            'birthdate': 'Date of birth',
            'email':'Email',
            'phone_number':'Phone',
            'address':'Address',
        }   


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-class', 'placeholder':"Enter trainers's name."}),
            'skills': forms.CheckboxSelectMultiple(),
            'last_name': forms.TextInput(attrs={'class':'form-class', 'placeholder':"Enter trainers's last name."}),
            'email': forms.EmailInput(attrs={'class':'form-class', 'placeholder':"Enter trainers's email."}),
            'address': forms.TextInput(attrs={'class':'form-class', 'placeholder':"Enter trainers's address."}),
            'birthdate': forms.DateInput(attrs={'class':'form-class', 'type':'date', 'placeholder':"Enter trainers's birthdate."}),

        }


