import requests
from celery import shared_task
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from imdb import Cinemagoer

ia = Cinemagoer()


@shared_task
def movie_data_from_api():
    from apps.movies.models import Movie as Movie_model

    r_data = requests.get('https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page=1&limit=1').json()
    last_page = r_data.get('last_page', 0)

    for page in range(1, last_page + 1):
        data = requests.get(f'https://videocdn.tv/api/movies?api_token=V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr&ordering=id&direction=des&page={page}&limit=100').json()
        movie_data = data.get('data', [])

        for content in movie_data:
            movie_list = ia.get_movie(content.get('imdb_id', '').split('tt')[1])
            imdb_id = content.get('imdb_id', '')
            image_url = movie_list['cover url']
            image_extension = image_url.split('.')[-1]
            file_name = f'{imdb_id}.{image_extension}'
            file_path = f'movies/posters/{file_name}'

            # Download the image file
            response = requests.get(image_url)
            content_file = ContentFile(response.content)

            # Save the image file using Django's default storage
            default_storage.save(file_path, content_file)

            objects = {
                'poster': file_path,
                'ru_title': content.get('ru_title', ''),
                'orig_title': content.get('orig_title', ''),
                'released_year': movie_list['year'],
                'rating': movie_list['rating'],
                'runtime': movie_list['runtime'][0],
                'iframe_src': 'https:' + content.get('iframe_src', ''),
                'kinopoisk_id': content.get('kinopoisk_id', ''),
                'imdb_id': imdb_id,
            }

            if not Movie_model.objects.filter(ru_title=objects['ru_title']).exists() and objects is not None:
                Movie_model.objects.create(**objects)
