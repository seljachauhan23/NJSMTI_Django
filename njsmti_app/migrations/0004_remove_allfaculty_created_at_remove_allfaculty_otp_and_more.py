# Generated by Django 4.2.5 on 2024-09-30 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njsmti_app', '0003_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allfaculty',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='allfaculty',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='allfaculty',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='material',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='material',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='query',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='query',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='replyquery',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='replyquery',
            name='updated_at',
        ),
    ]
