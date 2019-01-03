from django.urls import path

from history import views

urlpatterns = [
    path('delete/<int:pk>', views.HistoryDelete.as_view(), name='history_delete'),
    path('', views.HistoryList.as_view(), name='history'),
]