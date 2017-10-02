from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, PuppyViewSet, CreateUserView, FeedView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'puppies', PuppyViewSet)

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='register'),
    url(
        r'^feeds/(?P<username>[a-zA-Z0-9]{4,32})/',
        FeedView.as_view(),
        name='feed',
    ),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
