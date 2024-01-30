from rest_framework.pagination import PageNumberPagination

# from rest_framework.response import Response


class PostPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100

    # def get_paginated_response(self, data):
    #     return Response(
    #         {
    #             "count": self.page.paginator.count,
    #             "results": data,
    #         }
    #     )
