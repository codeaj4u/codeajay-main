
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("<slug:slug>/",views.singleblog,name="singleblog"),




]
