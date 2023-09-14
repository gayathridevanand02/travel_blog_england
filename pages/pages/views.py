from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):  # new
    template_name = "about.html"

class ContactPageView(TemplateView):  # new
    template_name = "contact.html"

class BlogPageView(TemplateView):  # new
    template_name = "blog.html"

class GalleryPageView(TemplateView):  # new
    template_name = "gallery.html"