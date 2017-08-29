from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #     views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
          views.show_category, name='show_category'),

]
    #This code imports the relevant Django
    # #machinery for URL mappings and the
    # views module from rango.
    # This allows us to call the function url
    # and point to the index view for the mapping in


