# Generated by Django 3.0.8 on 2021-02-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0035_auto_20210210_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialmodel',
            name='other_financiers',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
