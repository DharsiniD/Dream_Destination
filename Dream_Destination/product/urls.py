from django.urls import path
from . import views


urlpatterns=[
    path('',views.details,name="detail_page"),
    path('cmt/',views.commt,name='comments')
]