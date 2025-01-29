from django.db.models import Count
from django.core.paginator import Paginator
from ..serializers import TeamMemberSerializer


def team_members_paginator(query_response, context: dict, page: int, page_size: int):
    total_count = query_response.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(query_response, page_size)
    team_members = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(team_members),
        "first": not team_members.has_previous(),
        "last": not team_members.has_next(),
        "empty": total_count == 0,
        "content": TeamMemberSerializer(team_members, many=True, context=context).data,
    }

    return responses
