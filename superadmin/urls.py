from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index,name="superadmin"),
    path('traineraccount', views.traineraccount,name="traineraccount"),
    path('deletetraineraccount', views.deletetraineraccount,name="deletetraineraccount"),
    path('showedittrainer', views.showedittrainer,name="showedittrainer"),
    path('generatecode', views.generatecode,name="generatecode"),

    path('video', views.video,name="video"),
    path('deletevideo', views.deletevideo,name="deletevideo"),
    path('show_edit', views.show_edit,name="show_edit"),
    path('playlist', views.playlist,name="playlist"),
    path('series', views.series,name="series"),
    path('showmessageCourse', views.showmessageCourse,name="showmessageCourse"),
    path('deletecourse', views.deletecourse,name="deletecourse"),
    path('edit_showcourse', views.edit_showcourse,name="edit_showcourse"),
    path('feedback', views.feedback,name="feedback"),
    path('deletefeedback', views.deletefeedback,name="deletefeedback"),
    path('requests', views.requests,name="requests"),
    path('statusupdate', views.statusupdate,name="statusupdate"),
    path('updaterequestvideo', views.updaterequestvideo,name="updaterequestvideo"),
    path('requestvideo/<int:id>', views.requestvideo,name="requestvideo"),
    path('login', views.login,name="login"),
    path('forgetadminPassword', views.forgetadminPassword,name="forgetadminPassword"),
    path('forgetteacherpassword', views.forgetteacherpassword,name="forgetteacherpassword"),
    
    
    path('category', views.category,name="category"),
    path('showcategory', views.showcategory,name="showcategory"),
    path('deleteCategory', views.deleteCategory,name="deleteCategory"),
    path('payment', views.payment,name="payment"),
    path('logout', views.logout,name="logout"),
    path('Upload_Single_Videos', views.Upload_Single_Videos,name="Upload_Single_Videos"),
    path('deletesinglevideo', views.deletesinglevideo,name="deletesinglevideo"),
    path('show_edit_singlevideo', views.show_edit_singlevideo,name="show_edit_singlevideo"),
    path('contact', views.contact,name="contact"),
    path('deletecontact', views.deletecontact,name="deletecontact"),
    path('deleteplaylist', views.deleteplaylist,name="deleteplaylist"),
    path('editplaylist', views.editplaylist,name="editplaylist"),
    

    #teacherpanel

    path('teacherlogin', views.teacherlogin,name="teacherlogin"),
    path('Teacher_Panel', views.Teacher_Panel,name="Teacher_Panel"),
    path('referals', views.referals,name="referals"),
    path('studentadd', views.studentadd,name="studentadd"),
    path('deleteStudent', views.deleteStudent,name="deleteStudent"),
    path('showStudentDetail', views.showStudentDetail,name="showStudentDetail"),
    path('AddPlaylist/<int:id>', views.AddPlaylist,name="AddPlaylist"),
    path('RemovePlaylist/<int:id>', views.RemovePlaylist,name="RemovePlaylist"),
    path('exportuserdata', views.exportuserdata,name="exportuserdata"),
    path('exporttrainerdata', views.exporttrainerdata,name="exporttrainerdata"),
    path('forgetAdmin', views.forgetAdmin,name="forgetAdmin"),
    path('changerequest', views.changerequest,name="changerequest"),
    path('deleteCoursevideo', views.deleteCoursevideo,name="deleteCoursevideo"),


    

    

    




    
    


   ]