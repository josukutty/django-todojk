# Generated by Django 4.0.3 on 2022-03-31 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0004_delete_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='age',
        ),
    ]
