from django.db import models
import uuid  # Требуется для уникальных id таблиц
# Create your models here.

from django.urls import reverse  # Создание URL-адресов путем изменения шаблонов URL-адресов


class Type(models.Model):
    """Модель, представляющая тип документа"""
    name = models.CharField(
        'Тип документа',
        max_length=255,
        help_text="Введите тип документа"
    )

    def __str__(self):
        """Строка для представления объекта модели (в админке и т. д.)"""
        return self.name

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'


class Format(models.Model):
    """Модель, представляющая формат документа"""
    name = models.CharField(
        'Формат документа',
        max_length=255,
        help_text="Введите формат документа"
    )

    def __str__(self):
        """Строка для представления объекта модели (в админке и т. д.)"""
        return self.name

    class Meta:
        verbose_name = 'Формат документа'
        verbose_name_plural = 'Форматы документов'

class Classifier(models.Model):
    """Модель, представляющая отраслевой классификатор документа"""
    name = models.CharField(
        'Отраслевой классификатор документа',
        max_length=255,
        help_text="Введите отраслевой классификатор документа"
    )

    def __str__(self):
        """Строка для представления объекта модели (в админке и т. д.)"""
        return self.name

    class Meta:
        verbose_name = 'Отраслевой классификатор документа'
        verbose_name_plural = 'Отраслевые классификаторы документов'

class Technology(models.Model):
    """Модель, представляющая технологию"""
    name = models.CharField(
        'Технология документа',
        max_length=255,
        help_text="Введите технологию"
    )

    def __str__(self):
        """Строка для представления объекта модели (в админке и т. д.)"""
        return self.name

    class Meta:
        verbose_name = 'Технология документа'
        verbose_name_plural = 'Технологии документов'

class Language(models.Model):
    """Модель, представляющая язык"""
    name = models.CharField(
        'Язык документа',
        max_length=255,
        help_text="Введите язык"
    )

    def __str__(self):
        """Строка для представления объекта модели (в админке и т. д.)"""
        return self.name

    class Meta:
        verbose_name = 'Язык документа'
        verbose_name_plural = 'Языки документов'

class Book(models.Model):
    """Модель, представляющая документ (но не конкретный документ)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный идентификатор")
    id_doc = models.CharField('Код документа', max_length=255, help_text="Введите код документа")
    date_add = models.DateField(auto_now=True)
    short_name = models.CharField('Короткое название документа', max_length=255, help_text="Введите коротное название документа")
    autor = models.CharField('Автор документа', blank=True, max_length=255, help_text="Введите автора документа")
    isbn = models.CharField('ISBN документа', blank=True, max_length=13, unique=True, help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN номер</a>')
    bbk = models.CharField('ББК документа', blank=True, max_length=255, help_text="Введите ББК документа")
    udk = models.CharField('УДК документа', blank=True, max_length=255, help_text="Введите УДК документа")
    main_doc = models.BooleanField('Основной документа', default=0, help_text="(Да/Нет)")
    rel_date_doc = models.DateField('Дата выхода документа', help_text="Введите дату выхода документа")
    type_doc = models.ForeignKey('Type', on_delete=models.PROTECT, help_text="Выберите тип документа", verbose_name="Тип документа")
    original_source = models.CharField(blank=True, max_length=1000, help_text="Введите первоисточник документа", verbose_name="Первоисточник документа")
    short_desc = models.CharField(blank=True, max_length=255, help_text="Введите краткое описание документа", verbose_name="Краткое описание документа")
    language = models.ForeignKey('Language', on_delete=models.PROTECT, help_text="Выберите язык документа", verbose_name="Язык документа")
    format_doc = models.ForeignKey('Format', on_delete=models.PROTECT, help_text="Выберите формат документа", verbose_name="Формат документа")
    classifier_doc = models.ForeignKey('Classifier', on_delete=models.PROTECT, help_text="Выберите отраслевой классификатор документа", verbose_name="Отраслевой классификатор документа")
    technology_doc = models.ForeignKey('Technology', on_delete=models.PROTECT, help_text="Выберите технологию документа", verbose_name="Технология документа")
    file_doc = models.FileField(upload_to='docs/', blank=True, help_text="Выберите документ", verbose_name="Документ")

    class Meta:
        ordering = ['short_name']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def display_genre(self):
        """Создает строку для жанра. Это необходимо для отображения жанра в Admin."""
        #return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру книги."""
        #return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта модели."""
        return self.short_name