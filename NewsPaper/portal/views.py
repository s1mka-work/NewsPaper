from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    ordering = ['-date']
    template_name = 'posts.html'
    context_object_name = 'posts'

    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

def search_posts(request):
    posts = Post.objects.all()

    post_filter = PostFilter(request.GET, queryset=posts)

    return render(request, 'posts_search.html', {'filter': post_filter})

class BasePostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category = self.category
        post.author_id_id = 1
        post.save()


        self.object = post
        return HttpResponseRedirect('/news')

class NewsCreate(BasePostCreate):
    category = Post.news

class ArticlesCreate(BasePostCreate):
    category = Post.article

class BasePostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts_create.html'
    success_url = reverse_lazy('news_list')

    def get_queryset(self):
        return Post.objects.filter(category=self.category)

class NewsUpdate(BasePostUpdate):
    category = Post.news

class ArticlesUpdate(BasePostUpdate):
    category = Post.article

class BasePostDelete(DeleteView):
    model = Post
    template_name = 'posts_delete.html'
    success_url = reverse_lazy('news_list')

    def get_queryset(self):
        return Post.objects.filter(category=self.category)

class NewsDelete(BasePostDelete):
    category = Post.news

class ArticlesDelete(BasePostDelete):
    category = Post.article
