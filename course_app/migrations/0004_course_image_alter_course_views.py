# Generated by Django 5.0.5 on 2024-06-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_alter_course_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='Courses'),
        ),
        migrations.AlterField(
            model_name='course',
            name='views',
            field=models.IntegerField(null=True),
        ),
    ]