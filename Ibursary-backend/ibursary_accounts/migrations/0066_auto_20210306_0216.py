# Generated by Django 3.0.8 on 2021-03-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0065_auto_20210305_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trialmodel',
            old_name='first_name',
            new_name='applicant_full_name',
        ),
        migrations.AddField(
            model_name='bursaryapplicant',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
