# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home import restHtml

urlpatterns = [


    path("rest/dataset/table", restHtml.getDatasetTable, name="dataset_table"),
    path("rest/dataset/plot", restHtml.plotDataset, name="dataset_plot"),


    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),




]
