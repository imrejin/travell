from . import views

from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    #path('about/',views.about,name='about'),
    #path('details/',views.details,name='details'),
    #path('contact/',views.contact,name='contact'),
    #path('thanks/',views.thanks,name='thanks')
]
