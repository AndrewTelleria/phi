from django.urls import path

from . import views

urlpatterns = [
	path('', views.ordered_features, name="ordered_features"),
]