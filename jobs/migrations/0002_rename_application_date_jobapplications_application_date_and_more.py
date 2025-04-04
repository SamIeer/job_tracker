# Generated by Django 5.1.7 on 2025-04-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplications',
            old_name='Application_date',
            new_name='application_date',
        ),
        migrations.RenameField(
            model_name='jobapplications',
            old_name='Company_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='jobapplications',
            old_name='Job_title',
            new_name='job_title',
        ),
        migrations.RemoveField(
            model_name='jobapplications',
            name='Status',
        ),
        migrations.AddField(
            model_name='jobapplications',
            name='status',
            field=models.CharField(choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Rejected', 'Rejected'), ('Offer', 'Offer')], default='Applied', max_length=20),
        ),
    ]
