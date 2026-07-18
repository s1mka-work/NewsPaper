import django_filters
from django_filters import FilterSet
from django import forms
from .models import Post

class PostFilter(FilterSet):
    author = django_filters.CharFilter(field_name='author_id__user_id__username', lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Post
        fields = ['header', 'author', 'date']