from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


from .serializers import CarSerializer, CarAdminSerializers, DriveAdminSerializers,DriveSerializer
from .models import Car,Drive

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CarAdminSerializers

        else:
            return CarSerializer

class CarUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_url_kwarg = 'car_id'

    def get_object(self):
        car = self.queryset.get(pk=self.kwargs['car_id'])
        return car

#-----------------------------------------------Drive------------------

class DriveListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Drive.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return DriveAdminSerializers
        else:
            return DriveSerializer

class DriveUpdateDestryoyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer
    lookup_url_kwarg = 'drive_id'

    def get_object(self):
        drive = self.queryset.get(pk=self.kwargs['drive_id'])
        return drive



    
