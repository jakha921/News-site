from django.db import models
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):

    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def NewsDetailView(request, pk):
    print(pk)
    queryset = Articles.objects.filter(pk=pk)
    content = {"acricle": queryset}
    template_name = 'news/detail_view.html'
    context_object_name = 'article'
    return render(request, template_name, content)


def create(request):

    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была невенрной'

    form = ArticlesForm()

    data = {
        'form': form,
        # 'error': error
    }
    return render(request, 'news/create.html', data)
