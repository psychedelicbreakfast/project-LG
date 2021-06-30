from django.urls import path, include
from .views import List, Detail

urlpatterns = [
    path('<int:pk>/', Detail.as_view()),
    path('', List.as_view())
]
