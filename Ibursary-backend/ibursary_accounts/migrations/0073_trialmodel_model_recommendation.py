# Generated by Django 3.0.8 on 2021-03-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0072_auto_20210314_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialmodel',
            name='Model_Recommendation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
