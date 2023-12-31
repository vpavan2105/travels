from django.urls import path 
from .views import registration_view,login_view,logout_view,home_view,booking_view,agency_view,route_view,about_view

urlpatterns=[
    path('',home_view),
    path('agencies/',agency_view),
    path('booking/',booking_view),
    path('route/<int:id>',route_view),
    path('about/',about_view),
    path('register/',registration_view),
    path('accounts/login/',login_view),
    path('login/',login_view),
    path('logout/',logout_view),
]