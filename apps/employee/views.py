from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import serializers_Employee
from rest_framework import mixins
from rest_framework import generics
#CBV模式
class employee_view(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
                        ):

    queryset = Employee.objects.all()
    serializer_class = serializers_Employee
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) #需要使用restframeword的Response

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def post(self,request):
    #     serializer=serializers_Employee(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         print(serializer.data)
    #         return  Response({"msg":"请求成功",'code':'201'},status=status.HTTP_200_OK)
    #     return Response(serializer.error_messages,status=status.HTTP_404_NOT_FOUND)


