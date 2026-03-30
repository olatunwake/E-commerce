from django.urls import path
from .views import detail,new, delete

app_name = "item"

urlpatterns = [
    path('<int:pk>/', detail, name="detail"),
    path('<int:pk>/delete/', delete, name="delete"),
    path("new/",new, name="new"),
    ]