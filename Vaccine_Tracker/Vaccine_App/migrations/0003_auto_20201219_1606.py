# Generated by Django 3.0.3 on 2020-12-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vaccine_App', '0002_vaccinecenter_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinecenter',
            name='user',
        ),
        migrations.AddField(
            model_name='vaccinecenter',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='vaccinecenter',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccinecenter',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
