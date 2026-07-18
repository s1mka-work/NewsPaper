from django.urls import path
from .views import PostList, PostDetail, search_posts, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate, \
    ArticlesUpdate, ArticlesDelete

urlpatterns = [
    path('news', PostList.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetail.as_view()),
    path('news/search/', search_posts, name='search'),
    path('news/create/', NewsCreate.as_view(), name='create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='create'),
    path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='update'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='delete')
]