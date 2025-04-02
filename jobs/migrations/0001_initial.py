# Generated by Django 5.1.7 on 2025-04-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=200)),
                ('Job_title', models.CharField(max_length=200)),
                ('Application_date', models.DateField()),
                ('Status', models.CharField(choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Rejected', 'Rejected'), ('offer', 'offer')], default='Applied', max_length=20)),
            ],
        ),
    ]
