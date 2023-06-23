from autoslug import AutoSlugField
from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE, DateTimeField

from root.settings import AUTH_USER_MODEL


class Favourite(Model):
    user = ForeignKey(AUTH_USER_MODEL, CASCADE)
    movie = ForeignKey('Movie', CASCADE)


class History(Model):
    user = ForeignKey(AUTH_USER_MODEL, CASCADE)
    movie = ForeignKey('Movie', CASCADE)
    view_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-view_at']


class Movie(Model):
    ru_title = CharField(max_length=255)
    orig_title = CharField(max_length=255)
    released = CharField(max_length=15, null=True, blank=True)
    iframe_src = CharField(max_length=255, unique=True)
    imdb_id = CharField(max_length=25)
    kinopoisk_id = CharField(max_length=25)
    view_count = IntegerField(default=0)
    favourites_count = IntegerField(default=0)
    slug_link = AutoSlugField(populate_from='ru_title',
                              unique_with=['ru_title'])

    class Meta:
        unique_together = ['ru_title', 'orig_title']

    def __str__(self):
        return self.ru_title
