from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions,authentication
from .serializer import *
import json

# Create your views here.

      #       Authors

class Author_list_View(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,request,format=None):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

class Author_listid_View(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]

    def get(self,request,id,format=None):
        
        try:
            qs = Author.objects.get(id=id)
            
            serializer = AuthorSerializer(qs)
            print(serializer.data)
            return Response(serializer.data)
        except:
            return Response({"data":"no user with such id"})

class Author_post_View(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]

    def post(self,request,format=None):
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        Author.objects.create(first_name=firstname,last_name=lastname)
        return Response("Author created")

             #  BOOKS

class Book_list_View(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]
    queryset = Book.objects.all()

    def get(self,request,format=None):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data,)

class Book_listid_View(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]

    def get(self,request,id,format=None):
        queryset = Book.objects.get(id=id)
        serializer = BookSerializer(queryset)
        print(serializer.data)
        return Response(serializer.data)

class Book_post_View(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]

    def post(self,request,format=None):
        name = request.data['name']
        isbn = request.data['isbn']
        author = request.data['author']
        print(author)
        Book.objects.create(name=name,isbn=isbn,author_id=author)
        return Response("Book created")

# class RealtorIdView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     lookup_field = 'id'
#     def get_object(self,id):
#         try:
#             return Realtor.objects.get(id=id)
#         except Realtor.DoesNotExist:
#             raise Http404

#     def get(self,request,id,format=None):
#         qs = self.get_object(id)
#         serializer = RealtorSerializer(qs)
#         print(request.user)
#         return Response(serializer.data)