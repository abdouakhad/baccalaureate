# Generated by Django 3.2.6 on 2021-08-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liste', '0002_liste_choosen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liste',
            name='student_number',
            field=models.IntegerField(unique=True),
        ),
    ]
