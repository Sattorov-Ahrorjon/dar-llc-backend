from django.db.models import Count
from django.core.paginator import Paginator
from ..serializers import DarNewsSerializer


def dar_news_paginator(query_response, context: dict, page: int, page_size: int):
    total_count = query_response.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(query_response, page_size)
    dar_news = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(dar_news),
        "first": not dar_news.has_previous(),
        "last": not dar_news.has_next(),
        "empty": total_count == 0,
        "content": DarNewsSerializer(dar_news, many=True, context=context).data,
    }

    return responses
