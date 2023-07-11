# import concurrent.futures
#
# import httpx
# from celery import shared_task
# from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
# from django.db import transaction
# from imdb import IMDb
#
# ia = IMDb()
#
#
# @shared_task
# def movie_data_from_api():
#     from apps.movies.models import Movie as MovieModel
#     api_token = 'V5O2q1IlYYhqa3QFS5WOiKjj3xRLcihr'
#     base_url = 'https://videocdn.tv/api/movies'
#     page_limit = 100
#     batch_size = 10  # Number of movies to process in parallel
#
#     def fetch_movie_data(url):
#         with httpx.Client() as client:
#             response = client.get(url)
#             response.raise_for_status()
#             return response.json()
#
#     def download_and_save_image(url, file_path):
#         with httpx.Client() as client:
#             response = client.get(url)
#             response.raise_for_status()
#             content_file = ContentFile(response.content)
#             default_storage.save(file_path, content_file)
#
#     def process_movie(content):
#         try:
#             if not isinstance(content, dict):
#                 return
#
#             imdb_id = content.get('imdb_id', '')
#             if not imdb_id.startswith('tt'):
#                 return
#
#             movie_list = ia.get_movie(imdb_id[2:])
#             if not movie_list:
#                 return
#
#             with transaction.atomic():
#                 image_url = movie_list['cover url']
#                 image_extension = image_url.split('.')[-1]
#                 file_name = f'{content.get("ru_title", content.get("orig_title", imdb_id))}.{image_extension}'
#                 file_path = f'movies/posters/{file_name}'
#
#                 # Download and save the image file
#                 download_and_save_image(image_url, file_path)
#
#                 movie_data = {
#                     'poster': file_path,
#                     'ru_title': content.get('ru_title', ''),
#                     'orig_title': content.get('orig_title', ''),
#                     'released_year': movie_list['year'],
#                     'rating_imdb': movie_list['rating'],
#                     'runtime': movie_list['runtime'][0],
#                     'iframe_src': 'https:' + content.get('iframe_src', ''),
#                     'kinopoisk_id': content.get('kinopoisk_id', ''),
#                     'imdb_id': imdb_id,
#                 }
#
#                 movie = MovieModel(**movie_data)
#                 movie.save()
#
#         except Exception as e:
#             print(f"An exception occurred: {e}")
#             print(f"Content: {content}")
#
#     def process_batch(batch):
#         process_movie(batch)
#
#     def process_page(page):
#         url = f'{base_url}?api_token={api_token}&ordering=id&direction=des&page={page}&limit={page_limit}'
#         data = fetch_movie_data(url)
#         movie_data = data.get('data', [])
#         batched_data = [movie_data[i:i + batch_size] for i in range(0, len(movie_data), batch_size)]
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             executor.map(process_batch, batched_data[0])
#
#     def process_all_pages():
#         first_page_url = f'{base_url}?api_token={api_token}&ordering=id&direction=des&page=1&limit=1'
#         r_data = fetch_movie_data(first_page_url)
#         last_page = r_data.get('last_page', 0)
#         for page in range(1, last_page + 1):
#             process_page(page)
#
#     process_all_pages()
#
#
