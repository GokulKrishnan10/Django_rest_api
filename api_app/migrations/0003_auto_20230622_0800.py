# Generated by Django 3.2.19 on 2023-06-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_rename_rest_api_mysql_model_mysql_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysql_model',
            name='student_id',
        ),
        migrations.AddField(
            model_name='mysql_model',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
