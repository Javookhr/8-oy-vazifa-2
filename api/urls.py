from django.urls import path
from .views import CarListCreateView,CarUpdateDestroyApiView,DriveUpdateDestryoyApiView

urlpatterns = [
    path('cars/',CarListCreateView.as_view(),name='cars'),
    path('cars/<int:pk>/',CarUpdateDestroyApiView.as_view(),name='cars'),
    path('drives/<int:pk>/',DriveUpdateDestryoyApiView.as_view(),name='drives')
]

