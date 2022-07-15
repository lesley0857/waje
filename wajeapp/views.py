from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions,authentication
from .serializer import *

# Create your views here.

class Author_list_View(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [authentication.BasicAuthentication]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



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