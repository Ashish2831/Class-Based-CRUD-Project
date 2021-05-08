from django import forms
from .models import Student
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class Student_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False

    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'rollno' : 'Roll No',
            'rpassword': 'Confirm Password'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control'}),
            'rollno' : forms.TextInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'rpassword' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }

        required = ('name', 'email', 'rollno', 'password', 'rpassword')

    def clean_name(self):
        input_name = self.cleaned_data['name']
        if len(input_name.strip()) == 0:
            raise ValidationError(_("Please Enter Your Name")) 

        return input_name

    def clean_email(self):
        input_email = self.cleaned_data['email']
        
        validator = EmailValidator(_("Please Provide a Valid Email"))
        validator(input_email)

        return input_email

    def clean_rollno(self):
        input_rollno = self.cleaned_data['rollno']
        if input_rollno == None:
            raise ValidationError(_("Please Enter Your Roll No")) 

        return input_rollno

    def clean_password(self):
        input_password = self.cleaned_data['password']
        
        if len(input_password) == 0:
            raise ValidationError(_("Please Enter Your Password"))

        if len(input_password) < 8:
            raise ValidationError(_("Password must be greater than 8 characters"))

        return input_password

    def clean_rpassword(self):
        input_rpassword = self.cleaned_data['rpassword']
        input_password = self.data['password']

        if input_rpassword == None:
            raise ValidationError(_("Please Re-Enter Your Password"))

        if input_password != input_rpassword:
            raise ValidationError(_("Password must Matched"))

        return input_rpassword

