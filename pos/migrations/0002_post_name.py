# Generated by Django 3.0 on 2021-06-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]