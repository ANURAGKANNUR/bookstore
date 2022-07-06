
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from .views import BookListAV,BookdetailAV,registration_view,logout_view


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='log-out'),
    path('list/', BookListAV.as_view(), name="book-list"),
    path('<int:pk>', BookdetailAV.as_view(), name='book-detail'),
]
