from django.db import models
from django.urls import reverse

# Create your models here.

class FilmNews(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")#строковое поле с ограничением кол-ва ввода
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    content = models.TextField(blank=True)#бланк тру - можно ниче не передавать
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    ''' This is a Python function that returns the absolute URL for a specific object instance in Django 
      web framework. It uses the reverse function from django.urls module to generate the URL by 
      reversing the URL configuration. In this case, it reverses the 'posts_detail' view name and
       passes the keyword argument 'slug' with the value of the current object's slug attribute (self.slug).
        This method is commonly used in class-based 
      views (CBV) when you need to create links to detail pages for individual objects.'''

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name="название тэга")#строковое поле с ограничением кол-ва ввода
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

class Add(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name="Отзыв")  # строковое поле с ограничением кол-ва ввода
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


