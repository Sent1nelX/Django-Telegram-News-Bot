from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework import permissions, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from accounts.models import CustomUser, News
from accounts.serializers import CustomUserSerializer

from accounts.pars import get_html, proccessing, proccessing_table_2


# def start_pars_news(request):
#     html = get_html()
#     news_popular = proccessing_table_2(html)
#     news = proccessing(html)
    
#     if news and news_popular:
#         return HttpResponse("<h1>Парсинг окончен</h1>")
    
#     return HttpResponse("<h1>Парсинг не окончен</h1>")



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, 
            data=request.data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
