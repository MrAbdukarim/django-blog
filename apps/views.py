from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Posts


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PostPageView(ListView):
    model = Posts
    template_name = 'post.html'
