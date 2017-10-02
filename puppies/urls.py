from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, PuppyViewSet, CreateUserView, UsersPuppiesView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'puppies', PuppyViewSet)

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(
        r'^users/(?P<user_pk>[0-9]{1,3})/posts/',
        UsersPuppiesView.as_view(),
        name='feed',
    ),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
