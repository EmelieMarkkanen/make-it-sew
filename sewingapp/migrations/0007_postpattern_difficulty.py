# Generated by Django 3.2.18 on 2023-03-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewingapp', '0006_auto_20230303_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpattern',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Expert')], default=0),
        ),
    ]
