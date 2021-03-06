# Generated by Django 4.0.1 on 2022-01-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('email', models.EmailField(max_length=200, verbose_name='Электронная Почта')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата Редактирования')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=7, verbose_name='Статус')),
            ],
        ),
    ]
