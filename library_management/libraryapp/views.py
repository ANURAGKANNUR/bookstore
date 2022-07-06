from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from rest_framework import request
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import BookSerializer, RegistrationSerializer
# from .permissions import AdminOrReadOnly

@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)

        data={}

        if serializer.is_valid():
            account=serializer.save()
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get(user=account).key
            data[token]=token
        else:
            data=serializer.errors
        return Response(data)

@api_view(['POST',])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token_delete()
        return Response(status=status.HTTP_200_OK)

class BookListAV(APIView):
     def get(self,request):
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
     def post(self,request):
         book=BookSerializer(data=request.data)
         if book.is_valid():
             book.save()
             return Response(book.data)
         else:
             return Response(book.errors)




class BookdetailAV(APIView):
    def get(self,request,pk): #to search book by primary key
        book=Book.objects.get(pk=pk)
        serializer=BookSerializer(book)
        return Response(serializer.data)

    def put(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        data=Book.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_200_OK)