# Generated by Django 3.0.8 on 2020-10-31 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0013_auto_20201101_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedapplicationsmodel',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
