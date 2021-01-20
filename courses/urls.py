from django.urls import path, include
from . import views

urlpatterns = [
    path('coursedirect/',views.coursedirect,name='coursedirect'),
    path('businessdirect/', views.businessdirect, name='businessdirect'),
    path('mobiledirect/', views.mobiledirect, name='mobiledirect'),
    path('itdirect/', views.itdirect, name='itdirect'),
    path('archidirect/', views.businessdirect, name='archidirect'),
    path('marketingdirect/', views.marketingdirect, name='marketingdirect'),
    path('lifestyledirect/', views.lifestyledirect, name='lifestyledirect'),
    path('photographydirect/', views.photographydirect, name='photographydirect'),
    path('fitnessdirect/', views.fitnessdirect, name='fitnessdirect'),
    path('musicdirect/', views.musicdirect, name='musicdirect'),
    path('edirect/', views.edirect, name='edirect'),
    path('newsort/', views.newsort, name='newsort'),
    path('intermediatesort/', views.intermediatesort, name='intermediatesort'),
    path('advancedsort/', views.advancedsort, name='advancedsort'),
    path('beginnersort/', views.beginnersort, name='beginnersort'),
    path('viewcourse/', views.viewcourse, name='viewcourse'),
    path('submitreview/', views.review, name='submitreview'),
    path('viewtutorials/', views.playcourse, name='viewvideo'),
    path('ldirect/', views.listcourse, name='ldirect'),
    path('wupload/',views.wupload,name='wupload'),
    path('courseintro/',views.courseintro,name='courseintro'),
    path('check/',views.check,name='check'),
]