# Generated by Django 5.0.5 on 2024-06-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0002_rename_buy_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='snumber',
            field=models.IntegerField(null=True),
        ),
    ]
