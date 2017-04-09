import django_filters
from django.contrib.auth.models import User
from isisdata.models import IsisCBRole


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    roles = django_filters.ModelChoiceFilter(name='isiscbrole', queryset=IsisCBRole.objects.all())

    class Meta:
        model = User
        fields = [
            'username', 'roles', 'is_staff'
        ]
    o = django_filters.filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('username', 'username'),
            ('email', 'email'),
            ('isiscbrole', 'role'),
        ),

        # labels do not need to retain order
        field_labels={
            'username': 'Username',
        }
    )
