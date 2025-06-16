
import django_filters

from status.models import Status
from jobpost.models import JobPost
from .models import Application

class ApplicationFilter(django_filters.FilterSet):
    # Filtros para los campos relacionados
    jobpost_category = django_filters.NumberFilter(field_name='jobpost__category__id')
    status = django_filters.NumberFilter(field_name='status__id')
    applicant_username =  django_filters.CharFilter(field_name='applicant__username', lookup_expr='icontains')
    jobpost_title = django_filters.CharFilter(field_name='jobpost__title', lookup_expr='icontains')
    jobpost_location = django_filters.CharFilter(field_name='jobpost__location', lookup_expr='icontains')
    resume_link = django_filters.CharFilter(field_name='resume_link',lookup_expr='icontains')
    submission_date__gte = django_filters.DateFilter(field_name='submission_date', lookup_expr='gte')
    submission_date__lte = django_filters.DateFilter(field_name='submission_date', lookup_expr='lte')


    class Meta:
        model = Application
        fields = ['jobpost_category', 'jobpost_title', 'jobpost_location', 'submission_date__gte','submission_date__lte','status','resume_link','applicant_username']
