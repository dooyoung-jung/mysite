from django.urls import path
import file.views as views
urlpatterns = [
 path('upload1', views.upload1),
]

from django.urls import path
import file.views as views
urlpatterns = [
 path('download', views.download),
]