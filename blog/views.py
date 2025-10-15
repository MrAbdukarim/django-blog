from django.views.generic import ListView, DetailView
from .models import Post, About
from django.shortcuts import render


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def about_view(request):
    about = About.objects.first()
    lang = request.GET.get('lang', 'uz')

    if lang == 'en':
        title = about.title_en
        body = about.body_en
    else:
        title = about.title_uz
        body = about.body_uz

    context = {
        'title': title,
        'body': body,
        'about': about,
        'lang': lang,
    }
    return render(request, 'about.html', context)
