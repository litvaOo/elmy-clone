from django import forms
from .models import Job
from accounts.models import CustomUser


class JobForm(forms.Form):
    job_type = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)


class BookForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())
