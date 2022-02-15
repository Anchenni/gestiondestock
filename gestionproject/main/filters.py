import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from django_filters.widgets import RangeWidget



from .models import *


class ProductFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte', )
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	# numero = CharFilter(field_name='numero', lookup_expr='icontains')
	# montant = DecimalField(field_name='montant', lookup_expr='icontains')
	date_created = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

	class Meta:
		model = Product
		fields = {'info','id','model','categorie','status',}
		# exclude = ['date_created']
		