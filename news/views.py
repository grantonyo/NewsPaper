from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .forms import NewsForm
from .models import Post
from .filters import NewsFilter

class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 3

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

class NewsListFilter(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'newsfilter.html'
    context_object_name = 'posts'
    paginate_by = 3

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_Post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = "NW"
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_Post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = "NW"
        return super().form_valid(form)

# Представление удаляющее товар.
class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_Post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')



class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_Post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = "AR"
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_Post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = "AR"
        return super().form_valid(form)

# Представление удаляющее товар.
class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_Post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
