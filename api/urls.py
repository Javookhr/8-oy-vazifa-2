from django.urls import path
from .views import CarView, DriveView

urlpatterns = [
    path('cars/',CarView.as_view(),name='cars'),
    path('cars/<int:pk>/', CarView.as_view(), name='car_detail'),
    path('drive/',DriveView.as_view(),name='cars'),
    path('drive/<int:pk>/',DriveView.as_view(),name='drive_detail')

]