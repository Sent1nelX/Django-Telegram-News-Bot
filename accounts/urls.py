from rest_framework import permissions, routers

from accounts.views import CustomUserViewSet, start_pars_news
from django.urls import path


router = routers.DefaultRouter()

router.register('api/users', CustomUserViewSet, basename='users')

urlpatterns = [
    # path('', start_pars_news, name = 'start_pars_news'),
    
]

urlpatterns += router.urls