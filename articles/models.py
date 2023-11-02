from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)  # Максимальная длина заголовка статьи
    content = models.TextField()  # Текст статьи
    pub_date = models.DateTimeField('date published')  # Дата публикации статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с моделью пользователя Django

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']  # Сортировка статей по убыванию даты публикации
