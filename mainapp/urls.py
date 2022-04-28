
from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('' , index,name='index'),
    path('for_parents/', for_parentsPage, name='for_parents'),
    path('for_students/', for_studentsPage, name='for_students'),
    path('contacts/', contacts_page, name='contacts' )

]
