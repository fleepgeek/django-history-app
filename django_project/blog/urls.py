from django.urls import path

from blog import views

urlpatterns = [
    path('<int:pk>', views.PostDetail.as_view(), name='post'),
    path('', views.PostList.as_view(), name='posts'),
]