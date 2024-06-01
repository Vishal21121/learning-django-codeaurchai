from django import forms
from .models import ChaiVariety

class ChaiVarirtyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(),label="Select chai variety")