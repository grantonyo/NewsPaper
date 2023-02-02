from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateTimeInput

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
    dateCreation = DateTimeFilter(
        field_name="dateCreation",
        lookup_expr="gt",
        label="Новость не ранее",
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'}),
   )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
            'postCategory': ['exact'],
        }

