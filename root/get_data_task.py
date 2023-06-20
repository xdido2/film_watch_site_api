import requests
from celery import shared_task


@shared_task
def movie_data_form_api():
    from apps.movies.models import Movie
    r_data = requests.get(
        'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page=1&limit=1').json()
    last_page = r_data.get('last_page', 0)

    for page in range(1, last_page + 1):
        data = requests.get(
            f'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page={page}&limit=100').json()
        movie_data = data.get('data', [])

        for content in movie_data:
            objects = {
                'ru_title': content.get('ru_title', ''),
                'orig_title': content.get('orig_title', ''),
                'released': content.get('released', ''),
                'iframe_src': 'https:' + content.get('iframe_src', ''),
                'kinopoisk_id': content.get('kinopoisk_id', ''),
                'imdb_id': content.get('imdb_id', ''),

            }

            if not Movie.objects.filter(ru_title=objects['ru_title']).exists() and objects is not None:
                Movie.objects.create(**objects)
