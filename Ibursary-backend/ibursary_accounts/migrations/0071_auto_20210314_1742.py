# Generated by Django 3.0.8 on 2021-03-14 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0070_remove_bursaryapplicant_applicant_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trialmodel',
            name='first_name',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_bursaryapplicant': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='ibursary_accounts.BursaryApplicant'),
        ),
    ]
