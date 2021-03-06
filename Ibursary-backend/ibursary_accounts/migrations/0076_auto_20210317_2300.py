# Generated by Django 3.0.8 on 2021-03-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0075_auto_20210315_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trialmodel',
            name='guardian_as_financier',
        ),
        migrations.RemoveField(
            model_name='trialmodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='trialmodel',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='trialmodel',
            name='other_financier',
        ),
        migrations.RemoveField(
            model_name='trialmodel',
            name='other_financiers',
        ),
        migrations.RemoveField(
            model_name='trialmodel',
            name='well_wishers_as_financier',
        ),
        migrations.AddField(
            model_name='trialmodel',
            name='Bursary_Application_Status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trialmodel',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
