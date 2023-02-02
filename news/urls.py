from django.urls import path
from .views import NewsList, PostDetail, NewsListFilter, NewsCreate, NewsUpdate, NewsDelete, CategoryListView, subscriptions, subscribe


urlpatterns = [

   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_details'),
   path('search/', NewsListFilter.as_view(), name='news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('subscriptions/', subscriptions, name='subscriptions'),

]