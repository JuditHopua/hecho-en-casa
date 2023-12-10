# Generated by Django 4.2.7 on 2023-12-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promos', '0002_alter_promo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Posición de la imagen'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='image',
            field=models.ImageField(upload_to='promos', verbose_name='Imagen'),
        ),
    ]