from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import cached_property

#from django.contrib.auth.models import User
from usersapp.models import BlogUser
from django.conf import settings

# 3 типа наследования: abstract, классическое, proxy

class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.TextField(blank=True)

    class Meta:
        abstract = True

# Create your models here.
class Category(TimeStamp):
    name = models.CharField(max_length=16, unique=True, verbose_name = 'Имя')
    description = models.TextField(blank=True, verbose_name = 'Описание')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # Основные типы полей
    # дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логический
    # models.BooleanField
    # # Байты (blob)
    # models.BinaryField
    # # Картинка
    # models.ImageField
    # # Файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField

    def __str__(self):
        return self.name
class Tag(IsActiveMixin):
    name = models.CharField(max_length=16, unique=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=False)

# class Post(TimeStamp):
#     name = models.CharField(max_length=32, unique=True)
#     text = models.TextField()
#     # Связь с категорией
#     # один - много
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     # связь с тегом
#     tags = models.ManyToManyField(Tag)
#     # Два варианта хранения картинок
#     image = models.ImageField(upload_to='posts', null=True, blank=True)
#     user = models.ForeignKey(BlogUser, on_delete=models.CASCADE) # null=True, blank=True - добавить при ошибке базы
#     def __str__(self):
#         return self.name

class Post(TimeStamp, IsActiveMixin):
    objects = models.Manager()
    active_objects = ActiveManager()
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='category_posts')
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)  # Используйте settings.AUTH_USER_MODEL для ссылки на модель пользователя по умолчанию
    rating = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=False)


    @cached_property
    def get_all_tags(self):
        tags = Tag.objects.all()
        return tags
    def __str__(self):
        return self.name

    def has_image(self):
        # print('my image:', self.image)
        # print('type', type(self.image))
        return bool(self.image)

    def some_method(self):
        return 'hello from method'

    def __str__(self):
        return f'{self.name}, category: {self.category.name}'

    def display_tags(self):
        tags = self.tags.all()
        result = ';'.join([item.name for item in tags])
        return result

# Классическое наследование
class CoreObject(models.Model):
    name = models.CharField(max_length=32)

class Car(CoreObject):
    description = models.TextField()

class Toy(CoreObject):
    text = models.TextField()



class Imajes(models.Model):
    name = models.ImageField()
    description = models.TextField(blank=True)
    # связь с тегом
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Search(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Другие поля вашей модели

    def __str__(self):
        return self.title

