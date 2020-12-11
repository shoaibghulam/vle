from django.db import models
from rest_framework import serializers


STATUS=(
    ("active","Active"),
    ("inactive","In_Active"),
)
REQUEST_STATUS=(
    ("done","Done"),
    ("undone","Un_Done"),
)
SUBSCRIPTION=(
    ("yearly","Yearly"),
    ("monthly","Monthly"),
    ("notsubscribe","Not Subscribe to Any Package"),
)
DIFFICULTY=(
    ("beginner","Beginner"),
    ("moderate","Moderate"),
    ("intermediate","Intermediate"),
    ("advance","Advance"),
)
INTENSITY=(
    ("level1","Level_1"),
    ("level2","Level_2"),
    ("level3","Level_3"),
    ("level4","Level_4"),
)
SUBSCRIPTION=(
    ("yearly","Yearly"),
    ("monthly","Monthly"),
    ("notsubscribe","Not Subscribe to Any Package"),
)
PACKAGE=(
    ("yearly","Premium"),
    ("monthly","Monthly"),
    ("notsubscribe","Not Subscribe to Any Package"),
)
SUBJECT=(
    ("Request_to_Change_Title","Request to Change Title"),
    ("Request_to_Remove_Video","Request to Remove Video"),
    ("Request_to_Change_Title","Request to Change Title"),
    ("other","other"),
    

)


# Create your models here.
class AdminAccount(models.Model):
    SId = models.AutoField(primary_key=True)
    SFname=models.CharField(max_length=100, default="First Name")
    SLname=models.CharField(max_length=100, default="Last Name")
    SEmail=models.CharField(max_length=100, default="Email Name")
    SUsername=models.CharField(max_length=100, default="Username ")
    SPassword=models.TextField(max_length=3000, default="Password ")
    SContactNo=models.CharField(max_length=100, default="Contact no")
    SProfile= models.ImageField(upload_to='SuperAdmin/',default="dummy.jpg")
    Token=models.CharField(max_length=20, default="0000")
    def __str__(self):
        return self.SFname

class Trainer_Account(models.Model):
    Trainer_Account_Id=models.AutoField(primary_key=True)
    U_Fname=models.CharField(max_length=100, default="First Name")
    U_Lname=models.CharField(max_length=100, default="Last Name")
    U_Email=models.CharField(max_length=100, default="Email Name")
    Username=models.CharField(max_length=100, default="Username ")
    SPassword=models.TextField(max_length=3000, default="Password ")
    U_ContactNo=models.CharField(max_length=100, default="Contact no")
    U_Desc=models.TextField(default="No")
    Gender=models.CharField(max_length=100, default="Male")
    DOB=models.DateField(auto_now_add=True,blank=True, null=True)
    Joining_Date=models.DateField(auto_now_add=True,blank=True, null=True)
    Referal_Code=models.CharField(max_length=100, default="12345")
    U_Image= models.ImageField(upload_to='TrainerAccount/',default="dummy.jpg")
    Token=models.CharField(max_length=20, default="0000")
    Status=models.CharField(max_length=100, choices=STATUS,default="")
    role=models.CharField(max_length=100,default="Teacher")
    
    def __str__(self):
        return self.U_Fname

class Ser_Trainer(serializers.ModelSerializer):
    class Meta:
        model = Trainer_Account
        fields = '__all__'
class Package(models.Model):
    Package_Id=models.AutoField(primary_key=True)
    Package_subscription=models.CharField(max_length=100, choices=SUBSCRIPTION,default="")
    Amount=models.CharField(max_length=20,default="1")
    
    def __str__(self):
        return self.Package_subscription




class User_Account(models.Model):
    User_Account_Id=models.AutoField(primary_key=True)
    U_Fname=models.CharField(max_length=100, default="First Name")
    U_Lname=models.CharField(max_length=100, default="Last Name")
    U_Email=models.CharField(max_length=100, default="Email Name")
    Username=models.CharField(max_length=100, default="Username ")
    SPassword=models.TextField(max_length=3000, default="Password ")
    U_ContactNo=models.CharField(max_length=100, default="Contact no")
    U_Desc=models.TextField(default="No")
    Gender=models.CharField(max_length=100, default="Male")
    DOB=models.DateField(auto_now_add=True,blank=True, null=True)
    Joining_Date=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    U_Image= models.ImageField(upload_to='Useraccount/',default="dummy.jpg")
    Token=models.CharField(max_length=20, default="0000")
    Status=models.CharField(max_length=100, choices=STATUS,default="active")
    Subscription_Status=models.CharField(max_length=100, choices=STATUS,default="inactive")
    Refered_by_Trainer=models.ForeignKey(Trainer_Account , on_delete=models.CASCADE,blank=True,null=True)
    Package_Id=models.ForeignKey(Package , on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.U_Fname

class Ser_Student(serializers.ModelSerializer):
    class Meta:
        model = User_Account
        fields = '__all__'

class Card_detail(models.Model):
    Card_detail_Id=models.AutoField(primary_key=True)
    User_Id=models.ForeignKey(User_Account , on_delete=models.CASCADE)
    Card_number=models.CharField(max_length=100,default="0")
    Cvc=models.IntegerField(default="12345")
    Package_Id=models.ForeignKey(Package , on_delete=models.CASCADE)
    expiration_date=models.DateField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Charge_Day=models.DateTimeField(auto_now_add=True,blank=True, null=True)
   



class Category(models.Model):
    Category_Id=models.AutoField(primary_key=True)
    C_Name=models.CharField(max_length=100, default="Name")
    C_Image= models.ImageField(upload_to='Category/',default="dummy.jpg")
    Status=models.CharField(max_length=100, choices=STATUS,default="")
    def __str__(self):
        return self.C_Name

class Ser_Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Playlist(models.Model):
    Playlist_Id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=100, default="Title")
    Decsription=models.TextField(default="Desc")
    Image= models.ImageField(upload_to='Playlist/',default="dummy.jpg")
    
    def __str__(self):
        return self.Title

class Ser_playlist(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class Course(models.Model):
    Course_Id=models.AutoField(primary_key=True)
    Trainer_Id=models.ForeignKey(Trainer_Account , on_delete=models.CASCADE)
    Series_Image= models.ImageField(upload_to='Series_Image/',default="dummy.jpg")
    Series_Name=models.CharField(max_length=100, default="Name")
    Decsription=models.TextField(default="Desc")
    Category_Id=models.ForeignKey(Category , on_delete=models.CASCADE)
    Difficulty=models.CharField(max_length=100, choices=DIFFICULTY,default="")
    Intensity=models.CharField(max_length=100, choices=INTENSITY,default="")
    Status=models.CharField(max_length=100, choices=STATUS,default="")
    Subject=models.CharField(max_length=100, choices=SUBJECT,default="")
    Message=models.TextField(default="No Message")
    Playlist_Id=models.ForeignKey(Playlist , on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.Series_Name

class Ser_Course(serializers.ModelSerializer):
    trianer_name=serializers.ReadOnlyField(source="Trainer_Id.U_Fname")
    category_name=serializers.ReadOnlyField(source="Category_Id.C_Name")
    class Meta:
        model = Course
        fields = ('trianer_name','Series_Image','Series_Name','Decsription','category_name','Difficulty','Intensity','Status','Subject','Message')





class Subject_Video(models.Model):
    Subject_Video_Id=models.AutoField(primary_key=True)
    Trainer_Id=models.ForeignKey(Trainer_Account , on_delete=models.CASCADE)
    Course_Id=models.ForeignKey(Course , on_delete=models.CASCADE)
    Category_Id=models.ForeignKey(Category , on_delete=models.CASCADE)
    Title_Name=models.CharField(max_length=100, default="Title")
    Difficulty=models.CharField(max_length=100, choices=DIFFICULTY,default="")
    Intensity=models.CharField(max_length=100, choices=INTENSITY,default="")
    Decsription=models.TextField(default="Desc")
    Video=models.FileField(upload_to='Videos/',default="dummy.jpg")
    Thumbnail= models.ImageField(upload_to='Thumbnail/',default="dummy.jpg")
    created_at=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return self.Title_Name

class Ser_subject(serializers.ModelSerializer):
    trianer_name=serializers.ReadOnlyField(source="Trainer_Id.Trainer_Account_Id")
    category_name=serializers.ReadOnlyField(source="Category_Id.C_Name")
    series_name=serializers.ReadOnlyField(source="Course_Id.Series_Name")
    class Meta:
        model = Subject_Video
        fields = ('trianer_name','series_name','Title_Name','Difficulty','Intensity','Decsription','Video','Thumbnail','created_at','category_name')











class Feedback(models.Model):
    Feedback_id=models.AutoField(primary_key=True)
    User_Id=models.ForeignKey(User_Account , on_delete=models.CASCADE)
    Email=models.CharField(max_length=200,default="email")
    Subject=models.CharField(max_length=200,default="subject")
    message=models.CharField(max_length=200,default="message")
    Attachment=models.FileField(upload_to='Feedback/',default="dummy.jpg")
    def __str__(self):
        return self.Email


class Request(models.Model):
    Request_id=models.AutoField(primary_key=True)
    Trainer_Id=models.ForeignKey(Trainer_Account , on_delete=models.CASCADE)
    Subject_Video_Id=models.ForeignKey(Subject_Video , on_delete=models.CASCADE)
    Series_Id=models.ForeignKey(Course , on_delete=models.CASCADE)
    Subject=models.CharField(max_length=200,default="subject")
    message=models.CharField(max_length=200,default="message")
    created_at=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Status=models.CharField(max_length=100, choices=REQUEST_STATUS,default="undone")
    def __str__(self):
        return self.Subject


class Contact(models.Model):
    Contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, default="Last Name")
    Email=models.CharField(max_length=100, default="Email Name")
    ContactNo=models.CharField(max_length=100, default="Contact no")
    Message=models.TextField(default="No")
    def __str__(self):
        return self.name


class Single_Video(models.Model):
    Single_Video_id=models.AutoField(primary_key=True)
    Trainer_Id=models.ForeignKey(Trainer_Account , on_delete=models.CASCADE)
    Category_Id=models.ForeignKey(Category , on_delete=models.CASCADE)
    Title_Name=models.CharField(max_length=100, default="Title")
    Difficulty=models.CharField(max_length=100, choices=DIFFICULTY,default="")
    Intensity=models.CharField(max_length=100, choices=INTENSITY,default="")
    Decsription=models.TextField(default="Desc")
    Video=models.FileField(upload_to='Videos/',default="dummy.jpg")
    Thumbnail= models.ImageField(upload_to='Thumbnail/',default="dummy.jpg")
    created_at=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return self.Title_Name

class Ser_Single_Video(serializers.ModelSerializer):
    trianer_name=serializers.ReadOnlyField(source="Trainer_Id.Trainer_Account_Id")
    category_name=serializers.ReadOnlyField(source="Category_Id.C_Name")
    
    class Meta:
        model = Single_Video
        fields = ('trianer_name','Title_Name','Difficulty','Intensity','Decsription','Video','Thumbnail','created_at','category_name')

class Student_Favorite_Course(models.Model):
    Student_Favorite_id=models.AutoField(primary_key=True)
    Course_Id=models.ForeignKey(Course , on_delete=models.CASCADE,blank=True, null=True)
    Student_Id=models.ForeignKey(User_Account , on_delete=models.CASCADE,blank=True, null=True)
    
class Student_Favorite_Teacher(models.Model):
    Student_Favorite_Teacher_id=models.AutoField(primary_key=True)
    Teacher_Id=models.ForeignKey(Trainer_Account, on_delete=models.CASCADE,blank=True, null=True)
    Student_Id=models.ForeignKey(User_Account , on_delete=models.CASCADE,blank=True, null=True)

class Student_Favorite_Video(models.Model):
    Student_Favorite_Video_id=models.AutoField(primary_key=True)
    Video_id=models.ForeignKey(Single_Video , on_delete=models.CASCADE,blank=True, null=True)
    Student_Id=models.ForeignKey(User_Account , on_delete=models.CASCADE,blank=True, null=True)