# Generated by Django 3.2.8 on 2021-12-02 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycode', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='customer',
            name='userid',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
