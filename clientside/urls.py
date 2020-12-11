from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index,name="clientside"),
    path('about', views.about,name="about"),
    path('becometrainer', views.becometrainer,name="becometrainer"),
    path('contactus', views.contactus,name="contactus"),
    path('signin', views.signin,name="signin"),
    path('signup', views.signup,name="signup"),
    path('logout', views.logout,name="logout"),
    path('forgetpassword', views.forgetpassword,name="forgetpassword"),
    
    path('singlevideo', views.singlevideo,name="singlevideo"),
    path('showsinglevideo/<int:id>', views.showsinglevideo,name="showsinglevideo"),
    path('filterseries', views.filterseries,name="filterseries"),
    path('showcourse/<int:id>', views.showcourse,name="showcourse"),
    path('relatedCategory/<int:id>', views.relatedCategory,name="relatedCategory"),
    path('teacher', views.teacher,name="teacher"),
    path('user', views.user,name="user"),
    path('setting', views.setting,name="setting"),
    path('favorities', views.favorities,name="favorities"),
    path('showteacherprofile/<int:id>', views.showteacherprofile,name="showteacherprofile"),
    path('showcoursevideo/<int:id>', views.showcoursevideo,name="showcoursevideo"),
    path('videoplayer/<int:id>', views.videoplayer,name="videoplayer"),
    path('addtofavorite', views.addtofavorite,name="addtofavorite"),
    path('addtofavoritevideo', views.addtofavoritevideo,name="addtofavoritevideo"),
    path('addfavoriteteacher', views.addfavoriteteacher,name="addfavoriteteacher"),
    path('myfavorite', views.myfavorite,name="myfavorite"),
    path('deletefavoritecourse', views.deletefavoritecourse,name="deletefavoritecourse"),
    path('deletefavoritevideo', views.deletefavoritevideo,name="deletefavoritevideo"),
    path('deletefavoriteteacher', views.deletefavoriteteacher,name="deletefavoriteteacher"),
    path('playsinglevideo/<int:id>', views.playsinglevideo,name="playsinglevideo"),
    path('subscriptions', views.subscriptions,name="subscriptions"),
    path('payment/<int:id>', views.payment,name="payment"),
    path('Referencesignup/<int:id>', views.Referencesignup,name="Referencesignup"),
   
   

  
















    #####shakeeb######

      

  

    
]