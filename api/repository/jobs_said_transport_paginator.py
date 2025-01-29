from django.core.paginator import Paginator
from django.db.models import Count
from ..serializers import JobsSaidTransportSerializer


def jobs_said_transport_paginator(query_response, context: dict, page: int, page_size: int):
    total_count = query_response.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(query_response, page_size)
    jobs_said = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(jobs_said),
        "first": not jobs_said.has_previous(),
        "last": not jobs_said.has_next(),
        "empty": total_count == 0,
        "content": JobsSaidTransportSerializer(jobs_said, many=True, context=context).data,
    }

    return responses
