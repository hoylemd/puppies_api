from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, CreateUserView


users_router = routers.DefaultRouter()
users_router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(r'^', include(users_router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
