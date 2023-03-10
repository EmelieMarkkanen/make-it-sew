# Generated by Django 3.2.18 on 2023-03-10 19:28

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sewingapp', '0010_postpattern_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpattern',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='postpattern',
            name='suggested_fabrics',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('stretch', 'Stretch'), ('non_stretch', 'Non-stretch'), ('wool', 'Wool'), ('denim', 'Denim'), ('silk', 'Silk'), ('cotton', 'Cotton'), ('lace', 'Lace'), ('canvas', 'Canvas'), ('chiffon', 'Chiffon'), ('jersey', 'Jersey'), ('gingham', 'Gingham'), ('spandex', 'Spandex'), ('organza', 'Organza')], max_length=93, null=True),
        ),
    ]
