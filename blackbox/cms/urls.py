from django.urls import path

from blackbox.cms.views.pages.page_views import PageListView

urlpatterns = [
    path('pages/', PageListView.as_view(), name='page-list'),
]
