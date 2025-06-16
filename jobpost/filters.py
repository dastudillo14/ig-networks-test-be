import django_filters
from .models import JobPost
from django.contrib.auth.models import User
from category.models import Category

class JobPostFilter(django_filters.FilterSet):
    # Filtros para los campos relacionados
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), field_name='category')
    title = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por título (que contenga una cadena)
    location = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por ubicación (que contenga una cadena)
    created_by_username =  django_filters.CharFilter(field_name='created_by__username', lookup_expr='icontains')
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = JobPost
        fields = ['category', 'title', 'location', 'created_by_username','active','created_at__gte','created_at__lte']
