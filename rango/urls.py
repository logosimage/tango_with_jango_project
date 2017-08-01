from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
    #This code imports the relevant Django
    # #machinery for URL mappings and the
    # views module from rango.
    # This allows us to call the function url
    # and point to the index view for the mapping in


