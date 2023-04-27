from django.db import models


class Worker(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Картинка сотрудника')
    position = models.CharField(max_length=200, blank=True, null=True, verbose_name='Должность')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудники'



class Reviews(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Фото профиля')
    text = models.CharField(max_length=200, verbose_name='Отзыв')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Отзыв пользователя'
        verbose_name = 'Отзыв пользователя'


class Statistics (models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст')
    number = models.CharField(max_length=200, verbose_name='Количество')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Статистика'
        verbose_name = 'Статистика'