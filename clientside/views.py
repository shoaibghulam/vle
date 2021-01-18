from django.shortcuts import render, HttpResponse,redirect
from passlib.hash import pbkdf2_sha256
import json
import random
from django.contrib import messages
from superadmin.models import AdminAccount,Category,Ser_Category,User_Account,Trainer_Account,Ser_Trainer,Ser_Student,Course,Ser_Course,Subject_Video,Ser_subject,Feedback,Request,Playlist,Contact,Single_Video,Ser_Single_Video,Student_Favorite_Course,Student_Favorite_Teacher,Student_Favorite_Video,Package,Card_detail
from django.core.mail import send_mail,EmailMultiAlternatives
import stripe
import math as m
from datetime import date, timedelta
import calendar

#secrete key
stripe.api_key='sk_test_SD1VLYLcME6RYimXA3xxNKXW00eXfNnzuC'




# Create your views here.
def index(request):
    try:
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        recentcourse=Course.objects.all().order_by('-Course_Id')
        recentvideo=Single_Video.objects.all().order_by('-Single_Video_id')
        recentteacher=Trainer_Account.objects.all().order_by('-Trainer_Account_Id')
        return render(request,'clientside/index.html',{'recentcourse':recentcourse,'recentvideo':recentvideo,'recentteacher':recentteacher,'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'recentcourse':recentcourse,})
    except:
        return redirect('/clientside/')

def about(request):
    try:
        return render(request,'clientside/about.html')
    except:
        return redirect('/clientside/')

def becometrainer(request):
    try:
        if request.method=="POST":
            U_Email=request.POST['U_Email']
            checkrepeat=Trainer_Account.objects.filter(U_Email=U_Email)
            if checkrepeat:
                messages.error(request,"EmailAlready Exists")
                return redirect('/superadmin/traineraccount')
            U_Fname=request.POST['U_Fname']
            U_Lname=request.POST['U_Lname']
            Username=request.POST['Username']
            SPassword=request.POST['SPassword']
            U_ContactNo=request.POST['U_ContactNo']
            U_Desc=request.POST['U_Desc']
            Gender=request.POST['Gender']
            DOB=request.POST['DOB']
            U_Image=request.FILES['U_Image']
            Referal_Code=random.randint(1000,100000)
            data=Trainer_Account(U_Fname=U_Fname,U_Lname=U_Lname,U_Email=U_Email,Username=Username,SPassword=SPassword,U_ContactNo=U_ContactNo,U_Desc=U_Desc,Gender=Gender,DOB=DOB,U_Image=U_Image,Referal_Code=Referal_Code)
            data.save()
            messages.success(request,"Account Create Successfully")
            return redirect('/superadmin/teacherlogin')
        
            
                
        
        return render(request,'clientside/trainerRegister.html')
    except:
        return redirect('/clientside/')

def contactus(request):
    try:
        if request.method=="POST":
            name=request.POST['name']
            Email=request.POST['Email']
            ContactNo=request.POST['ContactNo']
            Message=request.POST['Message']
            data=Contact(name=name,Email=Email,ContactNo=ContactNo,Message=Message)
            data.save()
            return redirect('/clientside/contactus')
        
            
        return render(request,'clientside/contact.html')
    except:
        return redirect('/clientside/')

def signin(request):
    try:
        if request.method == "POST":
            U_Email = request.POST['email']
            SPassword = request.POST['password']
            print("this is my email ",U_Email , "and this is password",SPassword)
            checkAuthenticate = User_Account.objects.get(U_Email = U_Email)
            if checkAuthenticate:
                if checkAuthenticate.SPassword == SPassword:
                    try:
                        carddetail=Card_detail.objects.get(User_Id=checkAuthenticate.User_Account_Id)
                        expiredate=carddetail.expiration_date
                        today = date.today()
                        if today == expiredate:
                            
                            checkAuthenticate.Subscription_Status="inactive"
                            checkAuthenticate.Package_Id=None
                            checkAuthenticate.save()
                            return redirect('/')
                        elif checkAuthenticate.Status =="inactive":
                            messages.error(request,'Your Account has been Deactivate')
                            return redirect('/clientside/signin')
                        else:
                             request.session['userid'] = checkAuthenticate.User_Account_Id
                             request.session['userName'] = checkAuthenticate.Username
                             request.session['status'] =  checkAuthenticate.Status
                             return redirect('/clientside/favorities')

                    except:
                        request.session['userid'] = checkAuthenticate.User_Account_Id
                        request.session['userName'] = checkAuthenticate.Username
                        return redirect('/clientside/favorities')
                 


    except:
        messages.error(request,"Please Enter correct email and password")
        return redirect('/clientside/signin')
    
    

    ####get request
    if request.session.has_key('userid'):
        return redirect('/clientside/favorities')
        
  

    else:
        return render(request,'clientside/signin.html')
    

def forgetpassword(request):
    if request.method=="POST":
        U_Email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            try:
                check=User_Account.objects.get(U_Email=U_Email)
                if check:
                    check.U_Email=U_Email
                    check.SPassword=password1
                    check.save()
                    messages.success(request,"Password Updated Successfully")
                    return redirect('/clientside/signin')
                else:
                    messages.error(request,"Incorrect Email")
                    return redirect('/clientside/forgetpassword')
            except:
                messages.error(request,"Incorrect Email")
                return redirect('/clientside/forgetpassword')

                
        else:

            messages.success(request,"Password Does Not Match")
            return redirect('/clientside/forgetpassword')       
 
    return render(request,"clientside/forgetpassword.html")
        


def logout(request):
    del request.session['userid']
    del request.session['userName']
    
    return redirect('/clientside/')

def signup(request):
    try:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            gender = request.POST['gender']
            password = request.POST['password']
            dbirth = request.POST['dob']
            description = request.POST['U_Desc']
            images = request.FILES['image']
            checkEmailRepeat = User_Account.objects.filter(U_Email = email)
            if checkEmailRepeat:
                messages.error(request,"Email Already Exist")
                return redirect('/clientside/signup')
            userData = User_Account(U_Fname = fname,  U_Lname = lname,Username = username,U_Email = email, U_ContactNo = phone,Gender = gender,SPassword = password,DOB = dbirth,U_Desc = description,U_Image = images)
            userData.save()
            messages.success(request,"Signup Successfully")
            return redirect('/clientside/signin')
            


        return render(request,'clientside/signup.html')
    except:
        return redirect('/clientside/')


###signup through referencial

def Referencesignup(request,id):
    
    if request.method == "POST":
      
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']
        dbirth = request.POST['dob']
        description = request.POST['U_Desc']
        images = request.FILES['image']
        checkEmailRepeat = User_Account.objects.filter(U_Email = email)
        TeacherData = Trainer_Account.objects.get( Trainer_Account_Id = id)
        teacherID = TeacherData.Trainer_Account_Id
        if checkEmailRepeat:
            messages.error(request,"Email Already Exist")
            return redirect('Referencesignup',id = teacherID )
        
        userData = User_Account(U_Fname = fname,  U_Lname = lname,Username = username,U_Email = email, U_ContactNo = phone,Gender = gender,SPassword = password,DOB = dbirth,U_Desc = description,U_Image = images,Refered_by_Trainer = TeacherData)
        userData.save()
        messages.success(request,"Account Created Successfully")
        return redirect('/clientside/signin')



    TeacherData = Trainer_Account.objects.get( Trainer_Account_Id = id)
    return render(request,'clientside/referencesignup.html',{'teacher':TeacherData})
    # return HttpResponse(id)



    

def filterseries(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        if request.method == "POST":
            courseName = request.POST['coursename']
            data = Course.objects.filter(Series_Name__icontains = courseName)
            CategoryName = Category.objects.all()
            singlevideo=Single_Video.objects.all()
            Teacher=Trainer_Account.objects.all()
        
            return render(request,'clientside/filter-series.html',{'category':CategoryName,'singlevideo':singlevideo,'Teacher':Teacher,'course':data})

        
        else:
            # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
            # if user:
            #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
            #     expiredate=carddetail.expiration_date
            #     today = date.today()
            #     if today == expiredate:
            #         user.Subscription_Status="inactive"
            #         user.Package_Id=None
            #         user.save()

            CategoryName = Category.objects.all()
            singlevideo=Single_Video.objects.all()
            Teacher=Trainer_Account.objects.all()
            course=Course.objects.all()
            return render(request,'clientside/filter-series.html',{'category':CategoryName,'singlevideo':singlevideo,'Teacher':Teacher,'course':course})
    except:
        return redirect('/clientside/favorities')

def showcourse(request,id):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
    
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()  
        data=Course.objects.get(Course_Id=id)
        id=data.Course_Id
        Subject=Course.objects.get(Course_Id=id)
        
        
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        return render(request,'clientside/showallcourses.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'Sub':Subject})
    except:
        return redirect('/clientside/favorities')



###show Related category subject videos

def relatedCategory(request,id):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        subjectVideos = Course.objects.filter(Category_Id = id)
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()

        return render(request,'clientside/allcategoryvideos.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'relatedcategory':subjectVideos})
    except:
        return redirect('/clientside/favorities')

####show teacher profile

def showteacherprofile(request,id):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        teacherProfile = Trainer_Account.objects.get(Trainer_Account_Id = id)
        teacherCourses = Course.objects.filter(Trainer_Id = teacherProfile.Trainer_Account_Id)
        
        return render(request,'clientside/teacherProfile.html',{'teacherprofile':teacherProfile,'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'teachercourses':teacherCourses})

    except:
        return redirect('/clientside/favorities')
    


def singlevideo(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:

        if request.method == "POST":
            videoname = request.POST['videoname']
            data = Single_Video.objects.filter(Title_Name__icontains = videoname)
            CategoryName = Category.objects.all()
            subjectCourse = Subject_Video.objects.all()
            
            Teacher=Trainer_Account.objects.all()
            course=Course.objects.all()
            return render(request,'clientside/singlevideo.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':data,'Teacher':Teacher,'course':course})
        
        else:
            # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
            # if user:
            #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
            #     expiredate=carddetail.expiration_date
            #     today = date.today()
            #     if today == expiredate:
            #         user.Subscription_Status="inactive"
            #         user.Package_Id=None
            #         user.save()
            CategoryName = Category.objects.all()
            subjectCourse = Subject_Video.objects.all()
            singlevideo=Single_Video.objects.all()
            Teacher=Trainer_Account.objects.all()
            course=Course.objects.all()
            return render(request,'clientside/singlevideo.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course})
    except:
        return redirect('/clientside/favorities')

def showsinglevideo(request,id):

    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        data=Single_Video.objects.get(Single_Video_id=id)
        id=data.Single_Video_id
        Subjectvideo=Single_Video.objects.get(Single_Video_id=id)
        
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        return render(request,'clientside/showsinglevideo.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'s':Subjectvideo})

    except:
        return redirect('/clientside/favorities')

def teacher(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        return render(request,'clientside/teacher.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course})
    except:
        return redirect('/clientside/favorities')
def user(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        data=User_Account.objects.get(User_Account_Id=request.session['userid'])
        return render(request,'clientside/user.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'data':data})
    except:
        return redirect('/clientside/favorities')


def favorities(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
    
    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
       

     
            
    try:
        
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
            # try:
            #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
            #     expiredate=carddetail.expiration_date
            #     today = date.today()
            #     if today == expiredate:
            #         user.Subscription_Status="inactive"
            #         user.Package_Id=None
            #         user.save()
                    


        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()

        recentcourse=Course.objects.all().order_by('-Course_Id')
        recentvideo=Single_Video.objects.all().order_by('-Single_Video_id')


        return render(request,'clientside/favorities.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'recentcourse':recentcourse,'recentvideo':recentvideo})
    except:
        return redirect('/clientside/favorities')

def setting(request):
    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']
        
        description = request.POST['U_Desc']
        id=request.session['userid']
        getsignup = User_Account.objects.get(User_Account_Id = id)
        getsignup.U_Fname=fname
        getsignup.U_Lname=lname
        getsignup.Username=username
        getsignup.U_Email=email
        getsignup.U_ContactNo=phone
        getsignup.Gender=gender
        getsignup.SPassword=password
        
        getsignup.U_Desc=description
        getsignup.save()
        checkrepeat=User_Account.objects.filter(U_Email=email)
        if checkrepeat:
            messages.error(request,"Email Already Exists")
            return redirect('/clientside/user')
        else:
            checkrepeat.U_Email=U_Email
            checkrepeat.save()
        images = request.FILES['image']
        U_Image = request.FILES.get('images',False)
        if U_Image:
            getsignup.U_Image = U_Image
            getsignup.save()
        return redirect('/clientside/user')

    CategoryName = Category.objects.all()
    subjectCourse = Subject_Video.objects.all()
    singlevideo=Single_Video.objects.all()
    Teacher=Trainer_Account.objects.all()
    course=Course.objects.all()
    data=User_Account.objects.get(User_Account_Id=request.session['userid'])
    
    return render(request,'clientside/setting.html',{'data':data,'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course})

    
    

def showcoursevideo(request,id):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        
        data=Course.objects.get(Course_Id=id)
        id=data.Course_Id
        Subject=Subject_Video.objects.filter(Course_Id=id)
    
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        return render(request,'clientside/new-series.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'s':data,'Subject':Subject})
    except:
        return redirect('/clientside/favorities')
def addtofavorite(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        id=request.GET['id']
        student_id=request.session['userid']
        Student=User_Account.objects.get(User_Account_Id=student_id)
        course=Course.objects.get(Course_Id=id)
        checkauthenticate=Student_Favorite_Course.objects.filter(Course_Id=course,Student_Id=Student)
        if checkauthenticate:
            return HttpResponse("Already Added ")

        else:
            data=Student_Favorite_Course(Course_Id=course,Student_Id=Student)
            data.save()
            return HttpResponse("Added Successfully")
    except:
        return redirect('/clientside/favorities')
def addtofavoritevideo(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        id=request.GET['id']
        student_id=request.session['userid']
        Student=User_Account.objects.get(User_Account_Id=student_id)
        course=Single_Video.objects.get(Single_Video_id=id)
        checkauthenticate=Student_Favorite_Video.objects.filter(Video_id=course,Student_Id=Student)
        if checkauthenticate:
            return HttpResponse("Already Added ")

        else:
            data=Student_Favorite_Video(Video_id=course,Student_Id=Student)
            data.save()
            return HttpResponse("Added Successfully")
    except:
        return redirect('/clientside/favorities')
def addfavoriteteacher(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()
        id=request.GET['id']
        student_id=request.session['userid']
        Student=User_Account.objects.get(User_Account_Id=student_id)
        teacher=Trainer_Account.objects.get(Trainer_Account_Id=id)
        checkauthenticate=Student_Favorite_Teacher.objects.filter(Teacher_Id=teacher,Student_Id=Student)
        if checkauthenticate:
            return HttpResponse("Already Added ")

        else:
            data=Student_Favorite_Teacher(Teacher_Id=teacher,Student_Id=Student)
            data.save()
            return HttpResponse("Added Successfully")

    except:
        return redirect('/clientside/favorities')
def playsinglevideo(request,id):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

    # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end


    try:
        userid=request.session['userid']
        userdata=User_Account.objects.get(User_Account_Id=userid)
        carddetail=Card_detail.objects.filter(User_Id=userdata.User_Account_Id)
        if carddetail:
            carddetail=Card_detail.objects.get(User_Id=userdata.User_Account_Id)
            expiredate=carddetail.expiration_date
            today = date.today()
            if today > expiredate:
                userdata.Subscription_Status="inactive"
                userdata.Package_Id=None
                userdata.save()
                return redirect('/clientside/subscriptions')

            else:
                data=Subject_Video.objects.get(Subject_Video_Id=id)
                CategoryName = Category.objects.all()
                subjectCourse = Subject_Video.objects.all()
                singlevideo=Single_Video.objects.all()
                Teacher=Trainer_Account.objects.all()
                course=Course.objects.all()
                return render(request,'clientside/playsinglevideo.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'s':data})
                

        else:
            return redirect('/clientside/subscriptions')


            
    except:
        return redirect('/clientside/favorities')
def myfavorite(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        # user = User_Account.objects.get(User_Account_Id=request.session['userid'])
        # if user:
        #     carddetail=Card_detail.objects.get(User_Id=user.User_Account_Id)
        #     expiredate=carddetail.expiration_date
        #     today = date.today()
        #     if today == expiredate:
        #         user.Subscription_Status="inactive"
        #         user.Package_Id=None
        #         user.save()

        coursedata=Student_Favorite_Course.objects.filter(Student_Id=request.session['userid'])
        video=Student_Favorite_Video.objects.filter(Student_Id=request.session['userid'])
        teacher=Student_Favorite_Teacher.objects.filter(Student_Id=request.session['userid'])
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        return render(request,'clientside/myfavorite.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'coursedata':coursedata,'video':video,'teacher':teacher})

    except:
        return redirect('/clientside/favorities')
def deletefavoritecourse(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')
        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        id=request.GET['id']
        data=Student_Favorite_Course.objects.get(Student_Favorite_id=id)
        data.delete() 
        return HttpResponse("Delete Successfullly")
    except:
        return redirect('/clientside/favorities')
def deletefavoritevideo(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        id=request.GET['id']
        data=Student_Favorite_Video.objects.get(Student_Favorite_Video_id=id)
        return HttpResponse("Delete Successfullly")
    except:
        return redirect('/clientside/favorities')
def deletefavoriteteacher(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        id=request.GET['id']
        data=Student_Favorite_Teacher.objects.get(Student_Favorite_Teacher_id=id)
        data.delete()
        return HttpResponse("Delete Successfullly")
    except:
        return redirect('/clientside/favorities')
def subscriptions(request):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')

        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
       
        CategoryName = Category.objects.all()
        subjectCourse = Subject_Video.objects.all()
        singlevideo=Single_Video.objects.all()
        Teacher=Trainer_Account.objects.all()
        course=Course.objects.all()
        data=Package.objects.all()
        return render(request,'clientside/subscriptions.html',{'data':data,'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course})


       
    except:
        return redirect('/clientside/favorities')
def payment(request,id):
    if not request.session.has_key('userid'):
        return redirect('/clientside/signin')


        # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end
    try:
        if request.method == "POST":
            Card_number = request.POST['Card_number']
            Cvc = request.POST['Cvc']
            expiration_date = request.POST['expiration_date']
            charge = request.POST['charge']
            charge = float(charge)
            charge=m.ceil(charge*100)
        
            month = expiration_date[5:7]
            year=expiration_date[0:4]

            createtoken = stripe.Token.create(
            card={
            "number": Card_number,
            "exp_month": month,
            "exp_year":year ,
            "cvc": Cvc,
            },
            )


            charge = stripe.Charge.create(
            amount=charge,
            currency='usd',
            description='Virtual Learning Course charge',
            source = createtoken
            )

            
            if(charge['paid']==True):
                userid=request.session['userid']
                useraccount=User_Account.objects.get(User_Account_Id=userid)
                packageid=Package.objects.get(Package_Id=id)
                subscription=packageid.Package_subscription
                if subscription == "monthly":

                    today = date.today()
                    days_in_month = calendar.monthrange(today.year, today.month)[1]
                    oneMonthLater = today + timedelta(days=days_in_month)

                    check_Card_Detail = Card_detail.objects.filter(User_Id=userid)

                    if check_Card_Detail:

                        get_Data = Card_detail.objects.get(User_Id=userid)
                        get_Data.Card_number = Card_number
                        get_Data.Cvc = Cvc
                        get_Data.Package_Id = packageid
                        get_Data.expiration_date = oneMonthLater
                        get_Data.save()
                        return redirect('/clientside/favorities')       

                    else:

                        data=Card_detail(User_Id=useraccount,Card_number=Card_number,Cvc=Cvc,Package_Id=packageid,expiration_date=oneMonthLater)
                        data.save()
                        useraccount.Subscription_Status="active"
                        useraccount.Package_Id=packageid
                        useraccount.save()
                        return redirect('/clientside/favorities')






                    

                else:

                    check_Card_Detail = Card_detail.objects.filter(User_Id=userid)

                    if check_Card_Detail:
                        today = date.today()
                        AfterOneYear = today.replace(year = today.year + 1)

                        get_Data = Card_detail.objects.get(User_Id=userid)
                        get_Data.Card_number = Card_number
                        get_Data.Cvc = Cvc
                        get_Data.Package_Id = packageid
                        get_Data.expiration_date = AfterOneYear
                        get_Data.save()
                        return redirect('/clientside/favorities')  

                    else:  

                        today = date.today()
                        AfterOneYear = today.replace(year = today.year + 1)

                        data=Card_detail(User_Id=useraccount,Card_number=Card_number,Cvc=Cvc,Package_Id=packageid,expiration_date=AfterOneYear)
                        data.save()
                        useraccount.Subscription_Status="active"
                        useraccount.Package_Id=packageid
                        useraccount.save()
                        return redirect('/clientside/favorities')


                        
                        
        amount=Package.objects.get(Package_Id=id)
        price=amount.Amount
        request.session['price']=price
        charge=request.session['price']
        return render(request,'clientside/payment.html',{'charge':charge,'amount':amount})
    except:
        return HttpResponse("work")
        return redirect('clientside/favorities')

    

    
        

    
#  subject video player 
def videoplayer(request,id):
    if not request.session.has_key('userid'):
            return redirect('/clientside/signin')

            # account status checking code start
    if request.session.has_key('userid'):
        state=User_Account.objects.get(User_Account_Id=request.session['userid'])
        if state.Status=="inactive":
            messages.error(request,"Your Account has been Deactivate")
            return redirect('/clientside/logout')
    # account status checking code end


    try:
        userid=request.session['userid']
        userdata=User_Account.objects.get(User_Account_Id=userid)
        carddetail=Card_detail.objects.filter(User_Id=userdata.User_Account_Id)
        if carddetail:
            carddetail=Card_detail.objects.get(User_Id=userdata.User_Account_Id)
            expiredate=carddetail.expiration_date
            today = date.today()
            if today > expiredate:
                userdata.Subscription_Status="inactive"
                userdata.Package_Id=None
                userdata.save()
                return redirect('/clientside/subscriptions')

            else:
                data=Single_Video.objects.get(Single_Video_id=id)
                CategoryName = Category.objects.all()
                subjectCourse = Subject_Video.objects.all()
                singlevideo=Single_Video.objects.all()
                Teacher=Trainer_Account.objects.all()
                course=Course.objects.all()
                return render(request,'clientside/videoplayer.html',{'category':CategoryName,'subject':subjectCourse,'singlevideo':singlevideo,'Teacher':Teacher,'course':course,'data':data})
                

        else:
            return redirect('/clientside/subscriptions')


            
    except:
        return redirect('/clientside/favorities')
    
   