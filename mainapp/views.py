from django.shortcuts import render
from django.http import HttpResponse
from .models import  *


def index(request):
   slider = SwiperImg.objects.order_by('-id')[:6]
   mainPost = MainNewsPost.objects.order_by('-id')[:6]
   navbarspecial = NavbarDropdownSpeciality.objects.all()
   navbardigit = NavbarDropdownDigitarium.objects.all()
   navbarcolledge = NavbarDropdownColledge.objects.all()
   navbaraccept = NavbarDropdownAccept.objects.all()
   navbarspecialparents = NavbarDropdownParents.objects.all()
   navbarspecialstudents = NavbarDropdownStudents.objects.all()
   university = Aboutuniverse.objects.last()
   aboutPost = MainPost.objects.last()
   aboutPost2 =MainPostSecond.objects.last()
   aboutNumbers = MainTable.objects.order_by('-id')[:4]
   return render(request, 'index.html', {'slider': slider,"mainPost": mainPost, "navbar": navbarspecial,'navbar1':navbardigit,'navbar2':navbarcolledge,'navbar3':navbarcolledge,'navbar4':navbaraccept,'navbar5':navbarspecialparents,'navbar6': navbarspecialstudents,
   'aboutPost': aboutPost, 'aboutNumbers': aboutNumbers, 'aboutPost2':aboutPost2,'university': university })


def for_studentsPage(request):
   navbarspecial = NavbarDropdownSpeciality.objects.all()
   navbardigit = NavbarDropdownDigitarium.objects.all()
   navbarcolledge = NavbarDropdownColledge.objects.all()
   navbaraccept = NavbarDropdownAccept.objects.all()
   navbarspecialparents = NavbarDropdownParents.objects.all()
   navbarspecialstudents = NavbarDropdownStudents.objects.all()

   return render(request,'for_students.html',{"navbar": navbarspecial,'navbar1':navbardigit,'navbar2':navbarcolledge,'navbar3':navbarcolledge,'navbar4':navbaraccept,'navbar5':navbarspecialparents,'navbar6': navbarspecialstudents})

def for_parentsPage(request):
   navbarspecial = NavbarDropdownSpeciality.objects.all()
   navbardigit = NavbarDropdownDigitarium.objects.all()
   navbarcolledge = NavbarDropdownColledge.objects.all()
   navbaraccept = NavbarDropdownAccept.objects.all()
   navbarspecialparents = NavbarDropdownParents.objects.all()
   navbarspecialstudents = NavbarDropdownStudents.objects.all()
   forparents = ForParents.objects.all()
   return render(request,'for_parents.html',{"navbar": navbarspecial,'navbar1':navbardigit,'navbar2':navbarcolledge,'navbar3':navbarcolledge,'navbar4':navbaraccept,'navbar5':navbarspecialparents,'navbar6': navbarspecialstudents, 'forparents': forparents})

def contacts_page(request):

   return render(request,'contacts.html')