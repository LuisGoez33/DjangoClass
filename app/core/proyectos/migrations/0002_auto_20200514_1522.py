# Generated by Django 2.2.12 on 2020-05-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='ImgProye',
            field=models.ImageField(default='proyecto.png', upload_to='proyectos/img', verbose_name='Foto del proyecto'),
        ),
    ]
