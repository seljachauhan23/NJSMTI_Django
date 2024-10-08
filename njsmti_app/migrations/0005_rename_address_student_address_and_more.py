# Generated by Django 5.0.7 on 2024-09-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('njsmti_app', '0004_remove_allfaculty_created_at_remove_allfaculty_otp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Birth_place',
            new_name='birth_place',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Class',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='College',
            new_name='college',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Nationality',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Parents_mob',
            new_name='parents_mob',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Semester',
            new_name='semester',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Stud_mob',
            new_name='stud_mob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Dob',
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(default='2001-01-01'),
        ),
    ]
