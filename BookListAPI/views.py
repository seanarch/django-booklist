from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse

# # Create your views here.
# API view decorator in DRF 
@api_view(['GET','POST']) 
def books(request): 
    # return HttpResponse('list of the books', status=status.HTTP_200_OK)
    return Response('list of the books', status=status.HTTP_200_OK)

class BookList(APIView): 
    def get(self, request): 
        author = request.GET.get('author')
        if(author): 
            return Response({"message": "list of the books by " + author}, status.HTTP_200_OK)
        return Response({"message": "list of the books"}, status.HTTP_200_OK)
    
    def post(self, request): 
        # return Response({"message": "new book created"}, status.HTTP_201_CREATED)
        return Response({"title": request.data.get('title')}, status.HTTP_201_CREATED)

class Book(APIView): 
    def get(self, request, pk): 
        return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK) 
    
    def put(self, request, pk): 
        return Response({"title": request.data.get('title')}, status.HTTP_200_OK)