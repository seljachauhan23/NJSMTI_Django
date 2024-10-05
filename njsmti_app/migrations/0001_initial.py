# Generated by Django 4.2.5 on 2024-09-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=200)),
                ('Stud_mob', models.IntegerField(default=0)),
                ('Parents_mob', models.IntegerField(default=0)),
                ('Email', models.CharField(max_length=75)),
                ('Dob', models.DateField(default='01-01-2001')),
                ('Birth_place', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=40)),
                ('Gender', models.CharField(max_length=10)),
                ('Nationality', models.CharField(max_length=40)),
                ('College', models.CharField(max_length=50)),
                ('Course', models.CharField(max_length=40)),
                ('cgpa', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
