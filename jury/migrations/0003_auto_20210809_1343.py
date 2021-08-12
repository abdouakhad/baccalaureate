# Generated by Django 3.2.6 on 2021-08-09 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0002_jury_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jury',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='jury',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]