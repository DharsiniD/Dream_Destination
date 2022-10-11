from django.urls import path
from . import views


urlpatterns=[
    path('',views.details2,name="detail_page"),
    path('cmt/',views.commt,name='comments'),
    path('search/',views.search,name='search_box'),
    
]