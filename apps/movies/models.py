from autoslug import AutoSlugField
from django.db.models import Model, CharField


class Movie(Model):
    ru_title = CharField(max_length=255)
    orig_title = CharField(max_length=255)
    released = CharField(max_length=15, null=True, blank=True)
    iframe_src = CharField(max_length=255, unique=True)
    imdb_id = CharField(max_length=25)
    kinopoisk_id = CharField(max_length=25)
    slug_link = AutoSlugField(populate_from='ru_title',
                              unique_with=['ru_title'])

    class Meta:
        ordering = ['-id']
        unique_together = ['ru_title', 'orig_title']

    def __str__(self):
        return self.ru_title
