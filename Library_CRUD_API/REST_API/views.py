from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt




@api_view(['GET','POST'])
@csrf_exempt
def BookList(request):
    if request.method == 'GET':
        books=Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages,status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def BookDetail(request,book_Id):
    try:
        book=Book.objects.get(book_Id=book_Id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=BookSerializer(book,many=False)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'PUT':
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_200_OK)
    
