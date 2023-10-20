from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_check(text):
    if text != text.capitalize():
        raise ValidationError(
            _("%(text)s is not Capitalized"),
            params={"text": text},
        )

# Create your models here.
class Worker(models.Model):
    """Таблица с полями и их настройками в базе данных"""

    iin = models.CharField(verbose_name="ИИН", unique=True, max_length=13)
    first_name = models.CharField(verbose_name="Имя", max_length=200, validators=[validate_check])
    last_name = models.CharField(verbose_name="Фамилия", max_length=200, validators=[validate_check])