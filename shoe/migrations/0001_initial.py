# Generated by Django 4.2.10 on 2024-02-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Напишите понравившийся кроссовки')),
                ('description', models.TextField(verbose_name='Напишите описание кроссовка')),
                ('image_1', models.ImageField(upload_to='', verbose_name='Сюда вставлять ссылку на картинку')),
                ('image_2', models.ImageField(upload_to='', verbose_name='Сюда вставлять ссылку на картинку')),
                ('image_3', models.ImageField(upload_to='', verbose_name='Сюда вставлять ссылку на картинку')),
                ('brand', models.CharField(max_length=100, verbose_name='Напиши сюда бренд')),
                ('model', models.CharField(max_length=1000, verbose_name='Напиши какая модель кроссовка')),
                ('category', models.CharField(max_length=1000, verbose_name='Напиши для какой задачи сделаны кроссовки')),
                ('color', models.CharField(max_length=100, verbose_name='Напишите цвет кроссовка')),
                ('size', models.CharField(max_length=100, verbose_name='Напиши какие размеры доступны')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('discount', models.CharField(choices=[('10%', '10%'), ('20%', '20%'), ('50%', '50%'), ('75%', '75%')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]