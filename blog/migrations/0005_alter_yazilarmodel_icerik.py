# Generated by Django 4.2.3 on 2023-07-30 20:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_duzenleneme_tarihi_yazilarmodel_duzenlenme_tarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]