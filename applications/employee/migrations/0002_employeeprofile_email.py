# Generated by Django 3.2.12 on 2022-03-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
