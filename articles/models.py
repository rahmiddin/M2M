from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=15)
    articles = models.ManyToManyField(Article, related_name='articletag', through='Scope')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tег'
        verbose_name_plural = 'Теги'


class Scope(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes1')
    is_main = models.BooleanField(default=False)
