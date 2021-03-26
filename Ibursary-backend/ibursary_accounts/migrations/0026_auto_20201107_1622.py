# Generated by Django 3.0.8 on 2020-11-07 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0025_auto_20201107_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newapplicationmodel',
            name='user',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_bursaryapplicant': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='submittedapplicationsmodel',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_bursaryapplicant': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
