from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()  # Устанавливаем текущую дату и время
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('articles:article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('articles:article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('articles:article_list')