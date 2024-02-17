from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import EmpModel
from .serializer import EmpSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(http_method_names=['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def e_api(request):
    if request.method == 'POST':
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    emp = EmpModel.objects.all()
    serializer = EmpSerializer(emp, many=True)
    return Response(data=serializer.data)

@api_view(http_method_names=['GET','PUT','PATCH','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def e_detail_api(request, pk=None):
    epm = get_object_or_404(EmpModel, pk=pk)
    if request.method == 'GET':
        serializer = EmpSerializer(epm)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        epm.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = EmpSerializer(data=request.data, instance=epm)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = EmpSerializer(data=request.data, instance=epm, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)




