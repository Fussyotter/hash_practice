import string
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
from .models import Url
from .serializers import UrlSerializer
from .utils import base62_encode

# Create your views here.
# base62 encoding function


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        urls = Url.objects.all()
        serializer = UrlSerializer(urls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def redirect_view(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    url.count += 1
    url.save()
    return redirect(url.long_url)