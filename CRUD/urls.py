from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="Home"),
    path('update/<int:id>/', views.Update.as_view(), name="Update"),
    path('delete/<int:id>/', views.Delete.as_view(), name="Delete"),
]
