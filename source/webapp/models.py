from django.db import models

# Create your models here.

class GuestBook(models.Model):
    STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Электронная Почта')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата Редактирования')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return f"{self.pk}. {self.author}"