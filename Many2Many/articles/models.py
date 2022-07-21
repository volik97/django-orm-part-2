from django.db import models



class Article(models.Model): #Group

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Section(models.Model):

    tag_name = models.TextField(max_length=32, verbose_name='Название раздела')
    articles = models.ManyToManyField(Article, through='MainSection', related_name='sections')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name


class MainSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, related_name='section')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        ordering = ['section']