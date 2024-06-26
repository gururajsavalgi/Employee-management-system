# Generated by Django 5.0.3 on 2024-05-24 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_employee_dept_remove_employee_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='dept_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
    ]
