# Generated by Django 5.0.3 on 2024-05-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_role_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='location',
        ),
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
