from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),

]
    #This code imports the relevant Django
    # #machinery for URL mappings and the
    # views module from rango.
    # This allows us to call the function url
    # and point to the index view for the mapping in


