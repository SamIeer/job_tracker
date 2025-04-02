from django.db import models

# Model to store job applications
class JobApplications(models.Model):
    company_name = models.CharField(max_length=200)  # Changed to lowercase
    job_title = models.CharField(max_length=200)  # Changed to lowercase
    application_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Applied', 'Applied'),
            ('Interview', 'Interview'),
            ('Rejected', 'Rejected'),
            ('Offer', 'Offer')
        ],
        default='Applied'
    )

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"  # Fixed field names
