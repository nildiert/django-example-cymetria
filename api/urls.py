
from django.urls import path, include

from .views import HelloView

urlpatterns = [
    path('inventory/', HelloView.as_view()),
    path('inventory/<int:pk>/name/<str:name>', HelloView.as_view()),
]
