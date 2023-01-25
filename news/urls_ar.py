from django.urls import path
from .views import NewsList, PostDetail, NewsListFilter, ArticlesCreate, ArticlesUpdate, ArticlesDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', NewsListFilter.as_view(), name='articles_search'),
   path('create/', ArticlesCreate.as_view(), name='articles_create'),
   path('<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
   path('<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),



]