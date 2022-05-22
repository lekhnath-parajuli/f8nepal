from django import forms
from django.forms import ModelForm
from . import models

class addTeam(ModelForm):
    class Meta:
        model = models.Team
        fields = "__all__"
