from django.urls import path
from .import views

urlpatterns=[
    path('home',views.furniture_home),   
    path('page1',views.furniture_page1),
    path('hpage1',views.furniture_hpage1),
    path('hpage2',views.furniture_hpage2),
    path('page2',views.furniture_page2),
    path('hpage3',views.furniture_hpage3),
    path('hpage4',views.furniture_hpage4),
    path('hpage5',views.furniture_hpage5),
    path('hpage6',views.furniture_hpage6),
    path('page2',views.furniture_page2),
    path('page3',views.furniture_page3),
    path('page4',views.furniture_page4),
    path('page5',views.furniture_page5),
    path('page6',views.furniture_page6),
    path('page7',views.furniture_page7)
]
