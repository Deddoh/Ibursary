# Generated by Django 3.0.8 on 2020-10-31 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0012_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submittedapplicationsmodel',
            old_name='user',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='submittedapplicationsmodel',
            name='name',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
    ]
