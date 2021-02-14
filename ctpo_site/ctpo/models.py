from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
	def ger_qeryser(self):
		return super().get_queryset().filter(status='published')


class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'В работе'),
		('published', 'Опубликована'),
		)
	ON_MAIN_CHOICES = (
		('no','В базу'),
		('yes','На главную'),
	)
	title = models.CharField(max_length=250, verbose_name='Название')


	slug = models.SlugField(max_length=250,unique_for_date='publish')
	author = models.ForeignKey(User,on_delete=models.CASCADE,
	related_name='blog_posts')
	img = models.ImageField(null = True, blank = True,verbose_name='Превью изображение')
	body = models.TextField(verbose_name='Текст статьи')
	publish = models.DateTimeField(default=timezone.now, verbose_name='Дата')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft', verbose_name='Статус')
	on_main = models.CharField(max_length=10,choices=ON_MAIN_CHOICES,default='No', verbose_name='Позицианирование')
	
	bject = models.Manager()      # Стандарный менаджер
	published = PublishedManager() # Новый менаджер

	def get_absolute_url(self):
		return reverse('ctpo:post_detail', args=[self.publish.year,
			self.publish.month, self.publish.day, self.slug])
	

	


	class Meta:
		ordering = ('-publish',)
	
	def __str__(self):
		return self.title


class Training_programs(models.Model):

	title = models.CharField(max_length=250, verbose_name='Название')
	img = models.ImageField(null = True, blank = True, verbose_name='Изображение')
	sub_title = models.TextField(verbose_name='Краткое описание')
	body = models.TextField(verbose_name='Описание')
	
	object = models.Manager()
	
	def __str__(self):
		return self.title