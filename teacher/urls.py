from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index,name="teacherpannel"),
    path('series', views.series,name="series"),
    path('deletecourse/<int:id>', views.deletecourse,name="deletecourse"),
    path('edit_showcourse', views.edit_showcourse,name="edit_showcourse"),
    path('changerequest', views.changerequest,name="changerequest"),
    path('video', views.video,name="video"),
    path('deletevideo/<int:id>', views.deletevideo,name="deletevideo"),
    path('videoeditshow', views.videoeditshow,name="videoeditshow"),
    path('uploadsinglevideo', views.uploadsinglevideo,name="uploadsinglevideo"),
    path('deletesinglevideo/<int:id>', views.deletesinglevideo,name="deletesinglevideo"),
    path('show_edit_singlevideo', views.show_edit_singlevideo,name="show_edit_singlevideo"),
    path('logout', views.logout,name="logout"),
    
    

    
    


    


    





    
  

    
 ]