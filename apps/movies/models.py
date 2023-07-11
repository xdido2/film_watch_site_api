from autoslug import AutoSlugField
from django.db.models import Model, CharField, IntegerField, ImageField, FloatField


class Movie(Model):
    poster = ImageField(upload_to='movies/posters', null=True, blank=True)
    ru_title = CharField(max_length=255)
    orig_title = CharField(max_length=255)
    released_year = CharField(max_length=15, null=True, blank=True)
    rating_imdb = FloatField(max_length=5)
    runtime = IntegerField()
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
