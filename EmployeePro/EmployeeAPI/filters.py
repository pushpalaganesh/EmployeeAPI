import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='icontains')
    salary = django_filters.RangeFilter()
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')

    class Meta:
        model = Employee
        fields = ['emp_name', 'designation', 'salary']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset
