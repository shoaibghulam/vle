from django.contrib import admin
from .models import AdminAccount,User_Account,Trainer_Account,Category,Subject_Video,Course,Package,Card_detail,Feedback,Request,Playlist,Contact,Single_Video,Ser_Single_Video,Student_Favorite_Course,Student_Favorite_Teacher,Student_Favorite_Video

# Register your models here.
admin.site.register(AdminAccount)
admin.site.register(User_Account)
admin.site.register(Trainer_Account)
admin.site.register(Category)
admin.site.register(Playlist)
admin.site.register(Subject_Video)
admin.site.register(Course)
admin.site.register(Package)
admin.site.register(Card_detail)

admin.site.register(Feedback)
admin.site.register(Request)
admin.site.register(Single_Video)
admin.site.register(Contact)
admin.site.register(Student_Favorite_Course)
admin.site.register(Student_Favorite_Teacher)
admin.site.register(Student_Favorite_Video)
