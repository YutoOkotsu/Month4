# Generated by Django 4.2.10 on 2024-02-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='image_1',
            field=models.URLField(verbose_name='Сюда вставлять ссылку на картинку'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='image_2',
            field=models.URLField(verbose_name='Сюда вставлять ссылку на картинку'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='image_3',
            field=models.URLField(verbose_name='Сюда вставлять ссылку на картинку'),
        ),
    ]
