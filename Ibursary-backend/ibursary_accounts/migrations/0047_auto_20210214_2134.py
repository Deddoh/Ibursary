# Generated by Django 3.0.8 on 2021-02-14 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0046_auto_20210214_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialmodel',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_phone_trialmodel', to='ibursary_accounts.BursaryApplicant', unique=True),
        ),
        migrations.AlterField(
            model_name='trialmodel',
            name='last_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_last_trialmodel', to='ibursary_accounts.BursaryApplicant', unique=True),
        ),
    ]
