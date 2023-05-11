from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import APIGetTokenView, APISignUpView, ReviewViewSet, UsersViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path('v1/auth/token/', APIGetTokenView.as_view(), name='token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignUpView.as_view(), name='signup')
]
