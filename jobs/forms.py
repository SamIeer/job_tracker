from django import forms
from jobs.models import JobApplications

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplications
        fields = ['company_name', 'job_title', 'application_date', 'status']  # Fixed field names
