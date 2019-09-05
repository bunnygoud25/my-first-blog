from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('fb',views.fb,name='fb'),
    path('whatsapp',views.whatsapp,name='whatsapp'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('insta',views.insta,name='insta'),
    path('register',views.register,name='register'),

]
