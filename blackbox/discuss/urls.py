from django.urls import path

from blackbox.discuss.views.comments import CommentListView, CommentDetailsView

__author__ = 'Ashraful'

urlpatterns = [
    path('comments/', CommentListView.as_view(), name='comment-list-view'),
    path('comments/<str:uuid>/', CommentDetailsView.as_view(), name='comment-details-view'),
]
