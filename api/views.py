from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


from .serializers import CarSerializer,DriveSerializer
from .models import Car,Drive


class CarView(APIView):

    def get_car(self,pk):
        car = Car.objects.filter(pk=pk).first()

        if not car:
            raise NotFound(detail="Car topilmadi")

        return car

    def get(self,request:Request,pk=None):
        if pk:
            car = self.get_car(pk)

            serializer = CarSerializer(car)

            return Response(serializer.data)

        cars = Car.objects.all()

        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)

    def post(self,request:Request):
        serializer = CarSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message':"Malumotlar topilmadi"})

    def put(self,request:Request,pk):
        car = self.get_car(pk)

        serializer = CarSerializer(instance=car,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message':"Malumotlar yangilandi"})

    def patch(self,request:Request,pk):
        car = self.get_car(pk)

        serializer = CarSerializer(instance=car,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message':"Malumotlar yangilandi"})

    def delete(self,request:Request,pk):
        car = self.get_car(pk)

        car.delete()

        return Response({'message':"Malumotlar ochirildi"})

#------------------------------------Drive--------------------------------------------------------------

class DriveView(APIView):

    def get_drive(self,pk):
        drive = Drive.objects.filter(pk=pk).first()

        if not drive:
            raise NotFound(detail="Drive Topilmadi")

        return drive

    def get(self,request:Request,pk=None):
        if pk:
            drive = self.get_drive(pk)

            serializer = DriveSerializer(drive)

            return Response(serializer.data)

        drives = Drive.objects.all()

        serializer = DriveSerializer(drives,many=True)
        return Response(serializer.data)

    def post(self,request:Request):
        serializer = DriveSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message':"Malumotlar topildi"})

    def put(self,request:Request,pk):
        drive = self.get_drive(pk)

        serializer = DriveSerializer(instance=drive,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message':"Malumotlar yangilandi"})

    def patch(self,request:Request,pk):
        drive = self.get_drive(pk)

        serializer = DriveSerializer(instance=drive,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message'"Ma'lumotlar yangilandi"})

    def delete(self,request:Request,pk):
        drive = self.get_drive(pk)

        drive.delete()

        return Response({'message':"Ma'lumotlar ochirildi "})
