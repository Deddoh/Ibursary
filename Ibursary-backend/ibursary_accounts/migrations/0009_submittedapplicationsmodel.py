# Generated by Django 3.0.8 on 2020-10-23 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibursary_accounts', '0008_auto_20201018_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittedApplicationsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('admission_number', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('voter', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibursary_accounts.BursaryApplicant')),
            ],
        ),
    ]
