
from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('' , index,name='index'),
    path('for_parents/', for_parentsPage, name='for_parents'),
    path('for_students/', for_studentsPage, name='for_students'),
    path('contacts/', contacts_page, name='contacts' ),
    path('speciallity_page/' , speciallity_page, name='speciallity_page'),
    path('admission_page', admission_page, name='admission_page'),
    path('college', college, name='college'),
    path('college_historyPage', college_historyPage, name='college_historyPage'),
    path('base/', basePage, name='base')
]
