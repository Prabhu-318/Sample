from django.urls import path

from . views import *

urlpatterns=[
    path('',home_view,name='home'),
    path('create-student/',createstudent),
    path('delete-student/<id>',deletestudent),
    path('edit-student/<id>',editstudent),
]