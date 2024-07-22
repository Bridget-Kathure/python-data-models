# Generated by Django 5.0.6 on 2024-07-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=255)),
                ('class_capacity', models.SmallIntegerField(default=0)),
                ('class_schedule', models.TextField(blank=True)),
                ('class_attendance', models.TextField(blank=True)),
                ('class_projects', models.TextField(blank=True)),
                ('class_activities', models.TextField(blank=True)),
                ('class_representatives', models.TextField(blank=True)),
                ('class_policies', models.TextField(blank=True)),
                ('class_requirements', models.TextField(blank=True)),
                ('class_members_images', models.ImageField(blank=True, null=True, upload_to='classroom_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
