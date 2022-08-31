from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Наименование')
    content = models.TextField(blank=True, verbose_name= 'Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'Опубликовано') # текущая дата и время
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank= True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    # в кавычках так как
    # обьявлена позже
    # что бы изменить доступ к записям , related_name='get_news'

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs=dict(pk=self.pk))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name= 'Наименование категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['title']




