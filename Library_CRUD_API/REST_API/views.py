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
            return Response(data=request.data,status=status.HTTP_406_NOT_ACCEPTABLE)

    
