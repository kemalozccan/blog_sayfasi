# Generated by Django 4.2.3 on 2023-07-30 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_yazilarmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yazilarmodel',
            old_name='duzenleneme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
    ]
