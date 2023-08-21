from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentApi(APIView):
    def get(self,request,format=None):
        id=request.data.get('id',None)
        if id is not None:
            stu=StudentModel.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu=StudentModel.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created!'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTPS_401_NOT_CREATE)
    
    def put(self,request,format=None):
        data=request.data
        stu=StudentModel.objects.get(id=data.get('id'))
        serializer=StudentSerializer(stu ,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def delete(self, request,format=None):
        id=request.data.get('id')
        stu=StudentModel.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted !'})