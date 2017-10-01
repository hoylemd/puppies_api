from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, PuppyViewSet, CreateUserView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'puppies', PuppyViewSet)

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
