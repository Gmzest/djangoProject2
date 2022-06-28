# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('docs/', views.docs, name='docs'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('classifier/<str:classifier_doc>/', views.classifier_view, name='classifier_view'),
    path('technology/<str:technology_doc>/', views.technology_view, name='technology_view'),
    path('search/<str:parametr>/<str:value>', views.search_docs, name='search_docs'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]