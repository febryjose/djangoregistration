from registration.forms import RegistrationFormUniqueEmail
from django import forms
from .models import Profile


class ProfileForm(RegistrationFormUniqueEmail):
    passport = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
    	super(ProfileForm, self).__init__(*args, **kwargs)