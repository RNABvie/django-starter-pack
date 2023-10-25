import re

import django.contrib.auth.models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

def validate_check(text):
    if text != text.capitalize():
        raise ValidationError(
            _("%(text)s is not properly Capitalized"),
            params={"text": text},
        )
def validate_symbols(text):
    valid_txt = re.match(r"[A-Za-z]", text)

    if valid_txt is None:
        raise ValidationError(
            f"{text} contains prohibited symbols(use 'A-z')"
        )

def validate_numeric(str):
    try:
        int(str)
    except Exception:
        raise ValidationError(
            _("%(str)s contains symbols"),
            params={"str": str},
        )


####################################################

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"<Room({self.id}) name: {self.slug}>"


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_added',)

####################################################


class Worker(models.Model):
    """Таблица с полями и их настройками в базе данных"""

    iin = models.CharField(verbose_name="ИИН", unique=True, max_length=13, validators=[validate_numeric])
    first_name = models.CharField(verbose_name="Имя", max_length=200, validators=[validate_check, validate_symbols])
    last_name = models.CharField(verbose_name="Фамилия", max_length=200, validators=[validate_check, validate_symbols])

    class Meta:
        app_label = "djapp"
        ordering = ("iin",)
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return f"<Worker {self.id} {self.iin} {self.first_name}>"


class Rating(models.Model):
    """Таблица с полями и их настройками в базе данных 2"""
    post_id = models.BigIntegerField(verbose_name="Пост", unique=True)
    user_id = models.BigIntegerField(verbose_name="Пользователь")
    value = models.SmallIntegerField(verbose_name="Значение рейтинга", validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        app_label = "djapp"
        ordering = ("post_id", "user_id")
        verbose_name = "Отметка рейтинга"
        verbose_name_plural = "Отметки рейтинга"

    def __str__(self):
        return f"<Rating {self.post_id} {self.user_id} {self.value}>"


class News(models.Model):
    """Таблица с полями и их настройками в базе данных 3 """
    title = models.CharField(verbose_name="Наименование", unique=True, max_length=200)
    description = models.TextField(verbose_name="Описание", max_length=2000)
    datetime_created = models.DateTimeField(verbose_name="Дата публикации", default=now)

    class Meta:
        app_label = "djapp"
        ordering = ("-datetime_created",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"<News {self.title} {self.description[:10]}..>"






# class Author(models.Model):
#     name = models.CharField(max_length=100)
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#           #SET_NULL; PROTECT; DO_NOTHING; SET_DEFAULT; SET().
                    # when an Author instance is deleted, all
        #           related Book instances (belonging to that author)
                    # will be automatically deleted due to the CASCADE
        #           option specified in the ForeignKey field.


class UserProfile(models.Model):
    user = models.OneToOneField(
        editable=True,
        blank=True, #check it!!!!
        null=True,
        default=None,
        verbose_name="User's model....",
        to=User,
        on_delete=models.CASCADE,
        related_name="profile" # user.profile
    )
    abc = models.CharField(verbose_name="test text....", max_length=20, default='abcdXYZ')
    # avatar = models.ImageField(
    #     verbose_name="User's Avatar....",
    #     upload_to="static/media/users",
    #     default=None,
    #     null=True,
    #     blank=True
    # ) #INSTALL PILLOW FOR ImageField !!!
    class Meta:
        app_label = "auth"
        ordering = ('-user',)
        verbose_name = "User's profile...."
        verbose_name_plural = "Users' profiles"
    def __str__(self):
        return f"<UsProfile-_-{self.user.username}>"


@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
    # "created" will say to "get_or_create" to create or to
    # skip because of existing instance