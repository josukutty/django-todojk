# Generated by Django 4.0.3 on 2022-03-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myap', '0005_remove_details_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]