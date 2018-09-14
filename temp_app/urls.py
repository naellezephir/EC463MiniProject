from django.urls import path, include
from temp_app import views

urlpatterns = [
	path('', views.index, name='index'),
]