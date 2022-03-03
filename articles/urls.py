from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='post_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('articles/new/', ArticleCreateView.as_view(), name='post_new'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='post_edit'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='post_delete')

]