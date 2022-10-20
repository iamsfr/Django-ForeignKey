from django import forms
from django import forms
from .models import *

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'