# Generated by Django 2.1 on 2018-09-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0003_auto_20180918_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='publicacoes', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='mensagem',
            field=models.TextField(blank=True, help_text='Digite uma mensagem', verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='titulo',
            field=models.CharField(blank=True, help_text='Digite um título', max_length=30, null=True, verbose_name='Título'),
        ),
    ]
