# Generated by Django 2.1 on 2018-09-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0008_auto_20180918_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='nome',
        ),
    ]
