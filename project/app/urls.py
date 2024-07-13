from django.urls import path
from . import views

urlpatterns = [
    # path("home/",views.home,name='home'),
    path("dateTime/",views.filter_datetime,name='dateTime'),
    # path("float/",views.float_format,name='float'),
    # path("if_tag/",views.if_tag,name="if_tag") 
    # path("for_tag/",views.for_tag,name='for_tag'),    
]