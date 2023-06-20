from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'count_pages': self.page.paginator.num_pages,
            # 'currently_page': self.request.query_params['page'],
            # 'page_size': self.request.query_params['page_size'],
            'last_page': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
