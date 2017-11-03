from django.shortcuts import render
from school.models import School
from rest_framework import viewsets
from rest_framework import filters,pagination
from  school.serializers import SchoolSerializer
# Create your views here.
class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id')
    ordering = ('id')
    filter_fields = ('name',)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = "school"
    pagination.PageNumberPagination.pages_size = 100
    pagination.PageNumberPagination.paginate_by_param = 'pages_size'
    #pagination.CursorPagination.page_size = 100
    #pagination.LimitOffsetPagination.limit_query_param = 'limit'
    #pagination.LimitOffsetPagination.offset_query_param = 'offset'
    #pagination.CursorPagination.cursor_query_param  = 'cursor'
    #ordering = ['created']

