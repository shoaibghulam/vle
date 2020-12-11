from django.shortcuts import render, HttpResponse,redirect
from passlib.hash import pbkdf2_sha256
import json
import random
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from superadmin.models import AdminAccount,Category,Ser_Category,User_Account,Trainer_Account,Ser_Trainer,Ser_Student,Course,Ser_Course,Subject_Video,Ser_subject,Feedback,Request,Playlist,Contact,Single_Video,Ser_Single_Video,Student_Favorite_Course,Student_Favorite_Teacher,Student_Favorite_Video,Ser_playlist,Card_detail
from django.core.mail import send_mail,EmailMultiAlternatives
import xlwt


# Create your views here.
def index(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        studentData = User_Account.objects.all().order_by('-User_Account_Id')
        return render(request,'superadmin/users.html',{'data':studentData})
    except:
        return redirect('/superadmin/')
    



def exportuserdata(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['U_Fname', 'U_Lname', 'U_Email', 'Username','SPassword','U_ContactNo','U_Desc','Gender','Status']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = User_Account.objects.all().values_list('U_Fname', 'U_Lname', 'U_Email', 'Username','SPassword','U_ContactNo','U_Desc','Gender','Status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response
    except:
        return redirect('/superadmin/')



def exporttrainerdata(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Trainer.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['U_Fname', 'U_Lname', 'U_Email', 'Username','SPassword','U_ContactNo','U_Desc','Gender','DOB','Joining_Date','Status' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Trainer_Account.objects.all().values_list('U_Fname', 'U_Lname', 'U_Email', 'Username','SPassword','U_ContactNo','U_Desc','Gender','DOB','Joining_Date','Status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response
    except:
        return redirect('/superadmin/')







def traineraccount(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
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
            Status=request.POST['Status']
            Referal_Code=random.randint(1000,100000)
            data=Trainer_Account(U_Fname=U_Fname,U_Lname=U_Lname,U_Email=U_Email,Username=Username,SPassword=SPassword,U_ContactNo=U_ContactNo,U_Desc=U_Desc,Gender=Gender,DOB=DOB,U_Image=U_Image,Status=Status,Referal_Code=Referal_Code)
            data.save()
            messages.success(request,"Add Sucessfully")
            return redirect('/superadmin/traineraccount')


        data=Trainer_Account.objects.all().order_by('-Trainer_Account_Id')
        return render(request,'superadmin/traineraccount.html',{'data':data})
    except:
        return redirect('/superadmin/traineraccount')
       
        
            
    

def deletetraineraccount(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        id = request.GET['id']
        
        data=Trainer_Account.objects.filter(Trainer_Account_Id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        return redirect('/superadmin/traineraccount')
    
#show and Edit Category
def showedittrainer(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":

            
            U_Email=request.POST['U_Email']
            Trainerid=request.POST['Trainerid']
            U_Fname=request.POST['U_Fname']
            U_Lname=request.POST['U_Lname']
            Username=request.POST['Username']
            SPassword=request.POST['SPassword']
            U_ContactNo=request.POST['U_ContactNo']
            U_Desc=request.POST['U_Desc']
            Gender=request.POST['Gender']
            DOB=request.POST['DOB']
            Status=request.POST['Status']
            U_Email=request.POST['U_Email']
            gettrainer = Trainer_Account.objects.get(Trainer_Account_Id = Trainerid)
            gettrainer.U_Fname = U_Fname
            gettrainer.U_Lname = U_Lname
            gettrainer.Username = Username
            gettrainer.SPassword = SPassword
            gettrainer.U_ContactNo = U_ContactNo
            gettrainer.U_Desc = U_Desc
            gettrainer.Gender = Gender
            gettrainer.DOB = DOB
            gettrainer.Status = Status
            gettrainer.save()
            checkrepeat=Trainer_Account.objects.filter(U_Email=U_Email)
            if checkrepeat:
                pass
                # messages.success(request,"Update Trainer Sucessfully")
                # return redirect('/superadmin/traineraccount')
            else:
                gettrainer.U_Email=U_Email
                gettrainer.save()

            U_Image = request.FILES.get('U_Image',False)

            if U_Image:
                
                gettrainer.U_Image = U_Image
                gettrainer.save()

            
            messages.success(request,"Update Trainer Sucessfully")
            return redirect('/superadmin/traineraccount')





        trainerid = request.GET['id']
        userdata=list()
        trainerData = Trainer_Account.objects.get(Trainer_Account_Id = trainerid )
        mydata=(Ser_Trainer(trainerData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/traineraccount')
        
        


    

def generatecode(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "GET":
            user_id = request.GET['id']
            gettrainer = Trainer_Account.objects.get(Trainer_Account_Id = user_id)
            Referal_Code=random.randint(1000,100000)
            gettrainer.Referal_Code=Referal_Code
            gettrainer.save()
            messages.success(request,"New Code Generate Sucessfully")
            return HttpResponse('ok')
    except:
        return redirect('/superadmin/traineraccount')
    


def video(request):

    try:
        if request.method=="POST":
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.POST['Trainer_Id'])
            Course_Id=Course.objects.get(Course_Id=request.POST['Course_Id'])
            Category_Id=Category.objects.get(Category_Id=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            Video=request.FILES['Video']
            Thumbnail=request.FILES['Thumbnail']
            data=Subject_Video(Trainer_Id=Trainer_Id,Course_Id=Course_Id,Category_Id=Category_Id,Title_Name=Title_Name,Decsription=Decsription,Difficulty=Difficulty,Intensity=Intensity,Video=Video,Thumbnail=Thumbnail)
            data.save()
            messages.success(request,"Add Course Video Successfully")
            return redirect('/superadmin/video')
        Subject=Subject_Video.objects.all()
        trainer=Trainer_Account.objects.all()
        category=Category.objects.all()
        course=Course.objects.all()
        return render(request,'superadmin/video.html',{'trainer':trainer,'category':category,'course':course,'subject':Subject})
    except:
        return redirect('/superadmin/video')

        
    

def deletevideo(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        id = request.GET['id']
        data=Subject_Video.objects.get(Subject_Video_Id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        return redirect('/superadmin/video')

def show_edit(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            
            
            subjid=request.POST['subjid']
            subject=Subject_Video.objects.get(Subject_Video_Id=subjid)
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.POST['Trainer_Id'])
            subject.Course_Id=Course.objects.get(Course_Id=request.POST['Course_Id'])
            subject.Category_Id=Category.objects.get(C_Name=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            getsubject = Subject_Video.objects.get(Subject_Video_Id = subjid)
            getsubject.Trainer_Id = Trainer_Id
            getsubject.Course_Id = subject.Course_Id
            getsubject.Category_Id = subject.Category_Id

            getsubject.Title_Name = Title_Name
            getsubject.Difficulty = Difficulty
            getsubject.Intensity = Intensity
            getsubject.save()
            Thumbnail = request.FILES.get('Thumbnail',False)
            if Thumbnail:
                getsubject.Thumbnail = Thumbnail
                getsubject.save()
            Video = request.FILES.get('Video',False)
            if Video:
                getsubject.Video = Video
                getsubject.save()

            
            messages.success(request,"Update Course Video Sucessfully")
            return redirect('/superadmin/video')
        
        
        subjectid = request.GET['id']
        userdata=list()
        subjectData = Subject_Video.objects.get(Subject_Video_Id = subjectid )
        mydata=(Ser_subject(subjectData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/video')
    
    
def playlist(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            title = request.POST['title']
            description = request.POST['description']
            Image = request.FILES['thumbnail']
            checkExist = Playlist.objects.filter(Title = title)
            if checkExist:
                messages.error(request,"Already Exist")
                return redirect('/superadmin/playlist')
            else:
                
                playlistData = Playlist(Title = title,Decsription = description,Image = Image)
                playlistData.save()
                messages.success(request,"Added Sucessfully")
                return redirect('/superadmin/playlist')
        playlistData = Playlist.objects.all()
        return render(request,'superadmin/playlist.html',{'data':playlistData})
    except:
        return redirect('/superadmin/playlist')

    

def series(request):
    
  
    
    try:
        if request.method=="POST":
            Series_Image=request.FILES['Series_Image']
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.POST['Trainer_Id'])
            Series_Name=request.POST['Series_Name']
            Decsription=request.POST['Decsription']
            Category_Id=Category.objects.get(Category_Id=request.POST['Category_Id'])
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            Status=request.POST['Status']
            data=Course(Series_Image=Series_Image,Trainer_Id=Trainer_Id,Series_Name=Series_Name,Decsription=Decsription,Category_Id=Category_Id,Difficulty=Difficulty,Intensity=Intensity,Status=Status)
            data.save()
            messages.success(request,"Add Course Sucessfully")
            return redirect('/superadmin/series')


        trainer=Trainer_Account.objects.all()
        category=Category.objects.all()
        course=Course.objects.all()
        #teacher course and videos

        return render(request,'superadmin/series.html',{'trainer':trainer,'category':category,'course':course})
    except:
        return redirect('/superadmin/series')



def deleteCoursevideo(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        id = request.GET['id']
        data=Subject_Video.objects.get(Subject_Video_Id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        return redirect('/superadmin/video')


###Request changes

def changerequest(request):
    
    if request.method == "POST":
        courseID = request.POST['courseid']
        req_subject = request.POST['req_subject']
        message = request.POST['Request_Message']
        CourseData = Course.objects.get(Course_Id = courseID)
        CourseData.Message = message
        CourseData.Subject = req_subject
        CourseData.save()
        messages.success(request,'Response Record')
        return redirect('/superadmin/series')

     

      



    

def showmessageCourse(request):
  
    try:
        courseid = request.GET['id']
        userdata=list()
        courseData = Course.objects.get(Course_Id = courseid )
        mydata=(Ser_Course(courseData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/series')


def deletecourse(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        id = request.GET['id']
        
        data=Course.objects.filter(Course_Id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        return redirect('/superadmin/series')

def edit_showcourse(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            courseid=request.POST['courseid']
            CourseData = Course.objects.get(Course_Id = courseid)
            Trainer_Id = CourseData.Trainer_Id.Trainer_Account_Id
            Series_Name=request.POST['Series_Name']
            Decsription=request.POST['Decsription']
            CategoryName = request.POST['Category_Id']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            Status=request.POST['Status']
            CourseData.Trainer_Id = Trainer_Account.objects.get(Trainer_Account_Id = Trainer_Id)
            CourseData.Series_Name = Series_Name
            CourseData.Decsription = Decsription
            CourseData.Category_Id = Category.objects.get(C_Name = CategoryName)
            CourseData.Difficulty = Difficulty
            CourseData.Intensity = Intensity
            CourseData.Status = Status
            CourseData.save()
        
            Series_Image = request.FILES.get('Series_Image',False)
            if Series_Image:
                CourseData.Series_Image = Series_Image
                CourseData.save()

            
            messages.success(request,"Update Course Sucessfully")
            return redirect('/superadmin/series')
        courseid = request.GET['id']
        userdata=list()
        courseData = Course.objects.get(Course_Id = courseid )
        mydata=(Ser_Course(courseData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/series')

    

  

def feedback(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        feedback=Feedback.objects.all()
        return render(request,'superadmin/feedback.html',{'feedback':feedback})
    except:
        
        return redirect('/superadmin/feedback')

def deletefeedback(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        id = request.GET['id']
        data=Feedback.objects.filter(Feedback_id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        
        return redirect('/superadmin/feedback')


def requests(request):
  
    try:
        Userrequest=Request.objects.all()
        return render(request,'superadmin/requests.html',{'Userrequest':Userrequest})
    except:
        return redirect('/superadmin/requests')

def requestvideo(request,id):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        data=Request.objects.get(Request_id=id)
        video=data.Subject_Video_Id.Subject_Video_Id
        Subject=Subject_Video.objects.get(Subject_Video_Id=video)
        trainer=Trainer_Account.objects.all()
        category=Category.objects.all()
        course=Course.objects.all()
        return render(request,'superadmin/requestvideo.html',{'s':Subject,'trainer':trainer,'category':category,'course':course})
    except:
        return redirect('/superadmin/requestvideo')


def statusupdate(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "GET":
            requestvideo = request.GET['id']
            request = Request.objects.get(Request_id = requestvideo)
            request.Status="done"
            request.save()
            return HttpResponse('update')
    except:
        return redirect('/superadmin/requestvideo')
def updaterequestvideo(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            subjid=request.POST['subjid']
            subject=Subject_Video.objects.get(Subject_Video_Id=subjid)
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.POST['Trainer_Id'])
            subject.Course_Id=Course.objects.get(Series_Name=request.POST['Course_Id'])
            subject.Category_Id=Category.objects.get(C_Name=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            getsubject = Subject_Video.objects.get(Subject_Video_Id = subjid)
            getsubject.Trainer_Id = Trainer_Id
            getsubject.Course_Id = subject.Course_Id
            getsubject.Category_Id = subject.Category_Id

            getsubject.Title_Name = Title_Name
            getsubject.Difficulty = Difficulty
            getsubject.Intensity = Intensity
            getsubject.save()
            Thumbnail = request.FILES.get('Thumbnail',False)
            if Thumbnail:
                getsubject.Thumbnail = Thumbnail
                getsubject.save()
            Video = request.FILES.get('Video',False)
            if Video:
                getsubject.Video = Video
                getsubject.save()

            
            messages.success(request,"Update Course Video Sucessfully")
            return redirect('/superadmin/video')
        subjectid = request.GET['id']
        userdata=list()
        subjectData = Subject_Video.objects.get(Subject_Video_Id = subjectid )
        mydata=(Ser_subject(subjectData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/requestvideo')
    




def Upload_Single_Videos(request):
 
    try:
        if request.method=="POST":
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.POST['Trainer_Id'])
            Category_Id=Category.objects.get(Category_Id=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            Video=request.FILES['Video']
            Thumbnail=request.FILES['Thumbnail']
            data=Single_Video(Trainer_Id=Trainer_Id,Category_Id=Category_Id,Title_Name=Title_Name,Decsription=Decsription,Difficulty=Difficulty,Intensity=Intensity,Video=Video,Thumbnail=Thumbnail)
            data.save()
            messages.success(request,"Add Single Video Successfully")
            return redirect('/superadmin/Upload_Single_Videos')
        
        
        Subject=Single_Video.objects.all()
        trainer=Trainer_Account.objects.all()
        category=Category.objects.all()
        return render(request,'superadmin/Upload_Single_Video.html',{'trainer':trainer,'category':category,'subject':Subject})
    except:
        return redirect('/superadmin/Upload_Single_Videos')
   
    
   
    
    

def deletesinglevideo(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        id = request.GET['id']
        data=Single_Video.objects.get(Single_Video_id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        return redirect('/superadmin/Upload_Single_Videos')

  

def show_edit_singlevideo(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            
            
            subjid=request.POST['subjid']
            subject=Single_Video.objects.get(Single_Video_id=subjid)
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.POST['Trainer_Id'])
            
            subject.Category_Id=Category.objects.get(C_Name=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            getsubject = Single_Video.objects.get(Single_Video_id = subjid)
            getsubject.Trainer_Id = Trainer_Id
            
            getsubject.Category_Id = subject.Category_Id

            getsubject.Title_Name = Title_Name
            getsubject.Difficulty = Difficulty
            getsubject.Intensity = Intensity
            getsubject.save()
            Thumbnail = request.FILES.get('Thumbnail',False)
            if Thumbnail:
                getsubject.Thumbnail = Thumbnail
                getsubject.save()
            Video = request.FILES.get('Video',False)
            if Video:
                getsubject.Video = Video
                getsubject.save()

            
            messages.success(request,"Update Single Video Sucessfully")
            return redirect('/superadmin/Upload_Single_Videos')
        subjectid = request.GET['id']
        userdata=list()
        subjectData = Single_Video.objects.get(Single_Video_id = subjectid )
        mydata=(Ser_Single_Video(subjectData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/Upload_Single_Videos')
    
    
    

def login(request):
    try:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            checkAuthenticate = AdminAccount.objects.get(SEmail = email)
            if checkAuthenticate:
                if checkAuthenticate.SPassword == password:
                    request.session['adminid'] = checkAuthenticate.SId
                    request.session['userName'] = checkAuthenticate.SUsername
                    return redirect('/superadmin/')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect('/superadmin/login')

        return render(request,'superadmin/login.html')

    except:
        messages.error(request,"Incorrect Email")
        return redirect('/superadmin/login')


###forget admin####

def forgetAdmin(request):
    email = request.POST['email']
    html_content=f'''
            <h1 style="text-align:center; font-family: 'Montserrat', sans-serif;">Finish creating your account</h1>
                <p> 
        Your email address has been registered with lms. To validate your account and activate your ability to send email campaigns, please complete your profile by clicking the link below:</p>
            <div style='width:300px; margin:0 auto;'> <a href='http://127.0.0.1:8000/verification/435/shakeen' style=" background-color:#0066ff; border: none;  color: white; padding: 15px 32px;  text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; font-family: PT Sans, sans-serif;" >click here</a>
        </div>
            '''
        
    subject, from_email, to = 'Verify Account', 'no-replay@gwadarengineeringworks.com', email
    msgsend = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msgsend.attach_alternative(html_content, "text/html")
    msgsend.send()
    return HttpResponse('send')







    

def logout(request):

    try:

        del request.session['adminid']
        del request.session['userName']
        return redirect('/superadmin/login')
        
        
    except:
        return redirect('/superadmin/login')

    # if  request.session.has_key('teacherrole'):
    #     try:
    #         del request.session['trainerid']
    #         del request.session['userName']
    #         del request.session['teacherrole']
    #         return redirect('/superadmin/teacherlogin')
    #     except:
    #         return redirect('/superadmin/teacherlogin')

    # else:
    #     try:

    #         del request.session['adminid']
    #         del request.session['userName']
    #         return redirect('/superadmin/login')
    #     except:
    #         return redirect('/superadmin/login')



# teacher login
def teacherlogin(request):
    try:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            checkAuthenticate = Trainer_Account.objects.get(U_Email = email)
            if checkAuthenticate:
                if checkAuthenticate.SPassword == password:
                    request.session['trainerid'] = checkAuthenticate.Trainer_Account_Id
                    request.session['userName'] = checkAuthenticate.Username
                    request.session['teacherusername'] = checkAuthenticate.Username
                    request.session['teacherrole'] = checkAuthenticate.role
                    return redirect('/teacherpannel/')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect('/superadmin/teacherlogin')

        return render(request,'superadmin/teacherlogin.html')

    except:
        messages.error(request,"Incorrect Email")
        return redirect('/superadmin/teacherlogin')


def Teacher_Panel(request):
    if not request.session.has_key('trainerid'):
        return redirect('/teacherlogin/login')
    try:
        data=User_Account.objects.filter(Refered_by_Trainer=request.session['trainerid'])
        return render(request,'superadmin/referals.html',{'data':data})
    except:
        return redirect('/superadmin/Teacher_Panel')

    
    

def referals(request):
    if not request.session.has_key('trainerid'):
        return redirect('/teacherlogin/login')
    try:
        data=User_Account.objects.filter(Refered_by_Trainer=request.session['trainerid'])
        return render(request,'superadmin/referals.html',{'data':data})
    except:
        return redirect('/superadmin/referals')


def contact(request):
    if not request.session.has_key('adminid'):
        return redirect('/teacherlogin/login')
    try:
        data=Contact.objects.filter()
        return render(request,'superadmin/contact.html',{'data':data})
    except:
        return redirect('/superadmin/contact')

def deletecontact(request):
    if not request.session.has_key('adminid'):
        return redirect('/teacherlogin/login')
    try:
        id = request.GET['id']
        data=Contact.objects.filter(Contact_id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse("Delete")
    except:
        return redirect('/superadmin/contact')









####shakeeb######


def category(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            CategoryName = request.POST['categoryname']
            Status = request.POST['status']

            catImage = request.FILES['image']
            checkExist = Category.objects.filter(C_Name = CategoryName)
            if checkExist:
                messages.error(request,"Category Already Exist")
                return redirect('/superadmin/category')
            else:
                CategoryData = Category(C_Name = CategoryName,C_Image = catImage,Status=Status)
                messages.success(request,"Category Added Sucessfully")
                CategoryData.save()
                fetchData = Category.objects.all()
                return render(request,'superadmin/category.html',{'data':fetchData})


        fetchData = Category.objects.all().order_by('-Category_Id')
        return render(request,'superadmin/category.html',{'data':fetchData})
    except:
        
        return redirect('/superadmin/category')

    
    
    


#show and Edit Category
def showcategory(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            catId = request.POST['categoryId']
            CategoryName = request.POST['categoryname']
            Status = request.POST['status']
            getCategory = Category.objects.get(Category_Id = catId)
            getCategory.C_Name = CategoryName
            getCategory.Status = Status
            getCategory.save()
            catImages = request.FILES.get('image',False)
            if catImages:
                getCategory.C_Image = catImages
                getCategory.save()

            
            messages.success(request,"Update Category Sucessfully")
            return redirect('/superadmin/category')
            
            


        categoryId = request.GET['id']
        userdata=list()
        CategoryData = Category.objects.get(Category_Id = categoryId )
        mydata=(Ser_Category(CategoryData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/category')



def deleteCategory(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        categoryId = request.GET['id']
        CategoryData = Category.objects.get(Category_Id = categoryId )
        CategoryData.delete()
        messages.error(request,"Delete Category Sucessfully")
        return HttpResponse("Delete")
        # return redirect('/superadmin/category')
    except:
        return redirect('/superadmin/category')
   


def payment(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        data=Card_detail.objects.all()
        return render(request,'superadmin/payment.html',{'data':data})
    except:
        return redirect('/superadmin/payment')


def studentadd(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            image = request.FILES['image']
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            gender = request.POST['gender']
            # subscription = request.POST['subscription']
            # return HttpResponse(subscription)
            password = request.POST['password']
            dbirth = request.POST['dbirth']
            description = request.POST['description']
            status = request.POST['status']

            checkEmailRepeat = User_Account.objects.filter(U_Email = email)
            if checkEmailRepeat:
                messages.error(request,"Email Already Exist")
                return redirect('/superadmin/')


            

            studentData = User_Account(U_Fname = fname,U_Lname = lname,U_Email = email,Username = username,SPassword = password,U_ContactNo = phone,U_Desc = description,Gender = gender,DOB = dbirth,U_Image = image,Status = status)

            studentData.save()

            messages.success(request,"Sucessfully Add Student")
            return redirect('/superadmin/')
    except:
        return redirect('/superadmin/')



def deleteStudent(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        sid = request.GET['id']
        fetchStudnet = User_Account.objects.get(User_Account_Id = sid)
        fetchStudnet.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse('Delete')
    except:
        return redirect('/superadmin/')



def showStudentDetail(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            gender = request.POST['gender']
            # Subscription_Status = request.POST['subscription']
            password = request.POST['password']
            dbirth = request.POST['dbirth']
            description = request.POST['description']
            status = request.POST['status']
            studentId = request.POST['studentId']

            studentData = User_Account.objects.get(User_Account_Id = studentId)
            studentData.U_Fname = fname
            studentData.U_Lname = lname
            studentData.Username = username
            studentData.SPassword = password
            studentData.U_ContactNo = phone
            studentData.U_Desc = description
            studentData.Gender = gender
            studentData.DOB = dbirth
            studentData.Status = status
            # studentData.Subscription_Status = Subscription_Status
            studentData.save()

            image = request.FILES.get('image',False)
            if image:
                studentData.U_Image = image
                studentData.save()

            checkEmailpresent = User_Account.objects.filter(U_Email = email)
            if checkEmailpresent:
                messages.success(request,"Record Update Succesfully")
                return redirect('/superadmin/')
            else:
                studentData.U_Email = email
                studentData.save()
                messages.success(request,"Record Update Succesfully")
                return redirect('/superadmin/')



    ##########   Show Student Modal Data  ################
        sid = request.GET['id']
        userdata=list()
        fetchStudnet = User_Account.objects.get(User_Account_Id = sid)
        mydata=(Ser_Student(fetchStudnet))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/')
    
    


##Add playlist####

def AddPlaylist(request,id):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            playlistId = id
            courseid =  request.POST['id']
            coursevideo = Course.objects.get(Course_Id = courseid)
            coursevideo.Playlist_Id = Playlist.objects.get(Playlist_Id = playlistId)
            coursevideo.save()
            messages.success(request,"Add to Playlist Successfully")
            return HttpResponse("ADD")
        
        Subject=Subject_Video.objects.all()
        trainer=Trainer_Account.objects.all()
        category=Category.objects.all()
        course=Course.objects.all()
        playlist = id
        return render(request,'superadmin/addplaylist.html',{'trainer':trainer,'category':category,'course':course,'subject':Subject,'id':playlist})
    except:
        return redirect('/superadmin/playlist')




###Remove video from playlist

def RemovePlaylist(request,id):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        playlistId = id
        courseid =  request.POST['id']
        coursevideo = Course.objects.get(Course_Id = courseid)
        
        coursevideo.Playlist_Id = None
        coursevideo.save()
        messages.error(request,"Remove to Playlist Successfully")
        return HttpResponse('remove')
    except:
        return redirect('/superadmin/playlist')
# deleteplaylist
def deleteplaylist(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        playlistid = request.GET['id']
        delteplaylist = Playlist.objects.get(Playlist_Id = playlistid)
        delteplaylist.delete()
        messages.error(request,"Delete Sucessfully")
        return HttpResponse('Delete')
    except:
        return redirect('/superadmin/playlist')

def editplaylist(request):
    if not request.session.has_key('adminid'):
        return redirect('/superadmin/login')
    try:
        if request.method == "POST":
            Playlist_Id = request.POST['Playlist_Id']
            Title = request.POST['Title']
            Decsription = request.POST['Decsription']
            playlist = Playlist.objects.get(Playlist_Id = Playlist_Id)
            playlist.Title = Title
            playlist.Decsription = Decsription
        
            playlist.save()
            Image = request.FILES.get('Image',False)
            if Image:
                playlist.Image = Image
                playlist.save()

            
            messages.success(request,"Update Playlist Sucessfully")
            return redirect('/superadmin/playlist')
            
            


        playlist = request.GET['id']
        userdata=list()
        data = Playlist.objects.get(Playlist_Id = playlist )
        mydata=(Ser_playlist(data))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))
    except:
        return redirect('/superadmin/playlist')

def forgetadminPassword(request):
    if request.method=="POST":
        SEmail=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            try:
                check=AdminAccount.objects.get(SEmail=SEmail)
                if check:
                    check.SEmail=SEmail
                    check.SPassword=password1
                    check.save()
                    messages.success(request,"Password Updated Successfully")
                    return redirect('/superadmin/login')
                else:
                    messages.success(request,"Incorrect Email")
                    return redirect('/superadmin/login')
            except:
                messages.success(request,"Incorrect Email")
                return redirect('/superadmin/login')

                
        else:

            messages.success(request,"Password Does Not Match")
            return redirect('/superadmin/login')
            



        



    

def forgetteacherpassword(request):
    if request.method=="POST":
        U_Email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            try:
                check=Trainer_Account.objects.get(U_Email=U_Email)
                if check:
                    check.U_Email=U_Email
                    check.SPassword=password1
                    check.save()
                    messages.success(request,"Password Updated Successfully")
                    return redirect('/superadmin/teacherlogin')
                else:
                    messages.error(request,"Incorrect Email")
                    return redirect('/superadmin/teacherlogin')
            except:
                messages.error(request,"Incorrect Email")
                return redirect('/superadmin/teacherlogin')

                
        else:

            messages.success(request,"Password Does Not Match")
            return redirect('/superadmin/teacherlogin')
    
    
