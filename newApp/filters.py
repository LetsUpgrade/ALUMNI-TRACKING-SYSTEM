from .models import User
import django_filters


class AlumniFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    College = django_filters.CharFilter(lookup_expr='icontains')
    Year_Joined = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['College', 'Year_Joined']
