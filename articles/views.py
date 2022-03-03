from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

#list view
class ArticleListView(ListView):    
    template_name = "post_list.html"
    model = Article

#detail view
class ArticleDetailView(DetailView):
    template_name = "post_detail.html"
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "post_new.html"
    model = Article
    fields = ["title", "author", "body"]

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "post_edit.html"
    model = Article
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "post_delete.html"
    model = Article
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user