from django.urls import path,include
from . import views

urlpatterns = [
    path('InstructorSignup/', views.isignup, name='isignup'),
    path('UserSignup/', views.csignup, name='Signup'),
    path('Usersignin/' , views.csignin, name='Signin'),
    path('InstructorSignin/', views.isignin, name='isignin'),
    path('updatebio/',views.updatebio,name='updatebio'),
    path('updateimage/',views.updateimage,name='updateimage'),
    path('updatebilling/',views.updatebilling,name='updatebilling'),
    path('Userprofile/', views.Userdashboard, name='Userdashboard'),
    path('faq/', views.faq, name='faq'),
    path('term/', views.term, name='term'),
    path('pricing', views.pricing, name='pricing'),
]