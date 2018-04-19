from django.urls import path

from blackbox.cms.views.pages.content_views import ContentListView, ContentCreateView, ContentDetailsView
from blackbox.cms.views.pages.page_views import PageListView, PageDetailsView

urlpatterns = [
    path('pages/', PageListView.as_view(), name='page-list'),
    path('pages/<str:slug>/', PageDetailsView.as_view(), name='page-details'),
    path('contents/', ContentListView.as_view(), name='content-list'),
    path('contents/<str:slug>/', ContentDetailsView.as_view(), name='content-details'),
    path('create-content/', ContentCreateView.as_view(), name='content-create'),
]
