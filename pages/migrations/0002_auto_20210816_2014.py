# Generated by Django 3.2.6 on 2021-08-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='appreciations',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grades',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]