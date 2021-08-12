# Generated by Django 3.2.6 on 2021-08-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.PositiveIntegerField()),
                ('jury_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('serie', models.CharField(choices=[('L', 'L'), ('S', 'S'), ('T', 'T')], max_length=1)),
                ('department', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
    ]
