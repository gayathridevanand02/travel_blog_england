# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView,GalleryPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path("about/", AboutPageView.as_view(), name="about"),

    path("contact/", ContactPageView.as_view(), name="contact"),

    path("blog/", BlogPageView.as_view(), name="blog"),

    path("gallery/", GalleryPageView.as_view(), name="gallery"),

]