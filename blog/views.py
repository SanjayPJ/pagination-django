from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

# Create your views here.


class ArticleListView(ListView):
    model = Article
    paginate_by = 10