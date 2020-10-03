from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class AlumniSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_college = False
        if commit:
            user.save()
        return user


class CollegeSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_college = True
        # Verified = True
        if commit:
            user.save()
        return user


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "College",
            "About",
            "Work",
            "Year_Joined",
            "Branch",
            "Image"
        ]


class CollegeDetailsForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "College",
            "Image",
            "About",
            "Branch"
        ]
