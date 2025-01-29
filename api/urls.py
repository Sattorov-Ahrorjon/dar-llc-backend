from django.urls import path
from api import views

urlpatterns = [
    path('home/', views.MainViewSet.as_view({'get': 'homepage'}), name='homepage'),
]
