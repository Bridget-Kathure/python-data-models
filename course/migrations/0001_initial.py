# Generated by Django 5.0.6 on 2024-06-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.TextField()),
                ('course_description', models.TextField()),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('code', models.SmallIntegerField()),
                ('grading_system', models.TextField()),
                ('course_materials', models.TextField()),
                ('course_fee', models.SmallIntegerField()),
                ('course_outline', models.TextField()),
                ('course_language', models.TextField()),
            ],
        ),
    ]