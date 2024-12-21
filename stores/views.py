from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Store, Employee
from .serializers import StoreSerializer, EmployeeSerializer


class StoreView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        store= StoreSerializer(data = request.data)
        if store.is_valid():
            store.save()
            return Response(store.data, status = status.HTTP_201_CREATED)
        return Response(store.error, status = status.HTTP_400_BAD_REQUEST)
    
class StoreDetailView(APIView):
    def get(self, request, pk):
        store = Store.objects.get(pk = pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        employees= EmployeeSerializer(data = request.data)
        if employees.is_valid():
            employees.save()
            return Response(employees.data, status = status.HTTP_201_CREATED)
        return Response(employees.error, status = status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailView(APIView):
    def get(self, request, pk):
        employees = Employee.objects.get(pk = pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data, status = status.HTTP_200_OK)