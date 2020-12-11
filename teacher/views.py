from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
from superadmin.models import AdminAccount,Category,Ser_Category,User_Account,Trainer_Account,Ser_Trainer,Ser_Student,Course,Ser_Course,Subject_Video,Ser_subject,Feedback,Request,Playlist,Contact,Single_Video,Ser_Single_Video,Student_Favorite_Course,Student_Favorite_Teacher,Student_Favorite_Video,Ser_playlist,Card_detail
from django.contrib import messages
import json
# Create your views here.


##landing page
def index(request):
    try:
        if not request.session.has_key('trainerid'):
            return redirect('/superadmin/teacherlogin')

        data=User_Account.objects.filter(Refered_by_Trainer=request.session['trainerid'])
        return render(request,'teacher/referals.html',{'data':data})

    except:
        return redirect('/superadmin/teacherlogin')




##Add and show course
def series(request):
    try:
        if not request.session.has_key('trainerid'):
            return redirect('/superadmin/teacherlogin')


        if request.method=="POST":
            Series_Image=request.FILES['Series_Image']
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id = request.session['trainerid'])
            Series_Name=request.POST['Series_Name']
            Decsription=request.POST['Decsription']
            Category_Id=Category.objects.get(Category_Id=request.POST['Category_Id'])
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            Status=request.POST['Status']
            data=Course(Series_Image=Series_Image,Trainer_Id=Trainer_Id,Series_Name=Series_Name,Decsription=Decsription,Category_Id=Category_Id,Difficulty=Difficulty,Intensity=Intensity,Status=Status)
            data.save()
            messages.success(request,"Add Course Sucessfully")
            return redirect('/teacherpannel/series')
        
        
        else:
            course=Course.objects.filter(Trainer_Id = request.session['trainerid'])
            category=Category.objects.all()
            return render(request,'teacher/series.html',{'category':category,'course':course})

    except:
        return redirect('/teacherpannel')


##Delete Course
def deletecourse(request,id):
    try:
        fetchdata = Course.objects.get(Course_Id = id)
        fetchdata.delete()
        messages.error(request,"Delete Course Sucessfully")
        return redirect('/teacherpannel/series')
    
    except:
        return redirect('/teacherpannel')



##edit_course
def edit_showcourse(request):
    try:
        if request.method == "POST":
            courseid=request.POST['courseid']
            CourseData = Course.objects.get(Course_Id = courseid)
            Series_Name=request.POST['Series_Name']
            Decsription=request.POST['Decsription']
            CategoryName = request.POST['Category_Id']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            Status=request.POST['Status']
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
            return redirect('/teacherpannel/series')





        courseid = request.GET['id']
        userdata=list()
        courseData = Course.objects.get(Course_Id = courseid )
        mydata=(Ser_Course(courseData))
        userdata.append(mydata.data)
        return HttpResponse(json.dumps(userdata))

    
    except:
        return redirect('/teacherpannel')



# changerequest

def changerequest(request):
    try:
        if request.method == "POST":
            courseID = request.POST['courseid']
            req_subject = request.POST['req_subject']
            message = request.POST['Request_Message']
            CourseData = Course.objects.get(Course_Id = courseID)
            CourseData.Message = message
            CourseData.Subject = req_subject
            CourseData.save()
            messages.success(request,'Response Record')
            return redirect('/teacherpannel/series')

    except:
        return redirect('/teacherpannel')


##Trainer videos add and show
def video(request):
    try:
        if not request.session.has_key('trainerid'):
            return redirect('/superadmin/teacherlogin')

        if request.method=="POST":
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.session['trainerid'])
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
            return redirect('/teacherpannel/video')
        
        
        
        else:
            course=Course.objects.filter(Trainer_Id = request.session['trainerid'])
            category=Category.objects.all()
            Subject=Subject_Video.objects.filter(Trainer_Id = request.session['trainerid'])
            return render(request,'teacher/video.html',{"subject":Subject,"course":course,"category":category})

    except:
        return redirect('/teacherpannel')




#deletevideo
def deletevideo(request,id):
    try:
        fetchdata = Subject_Video.objects.get(Subject_Video_Id = id)
        fetchdata.delete()
        messages.error(request,"Delete Video Sucessfully")
        return redirect('/teacherpannel/video')

    except:
        return redirect('/teacherpannel')


###Edit Video
def videoeditshow(request):
    try:
        if request.method == "POST":
            subjid=request.POST['subjid']
            subject=Subject_Video.objects.get(Subject_Video_Id=subjid)
            subject.Course_Id=Course.objects.get(Course_Id=request.POST['Course_Id'])
            subject.Category_Id=Category.objects.get(C_Name=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            getsubject = Subject_Video.objects.get(Subject_Video_Id = subjid)
            getsubject.Course_Id = subject.Course_Id
            getsubject.Category_Id = subject.Category_Id
            getsubject.Title_Name = Title_Name
            getsubject.Difficulty = Difficulty
            getsubject.Intensity = Intensity
            getsubject.Decsription = Decsription
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
            return redirect('/teacherpannel/video')

        
        
        else:
            subjectid = request.GET['id']
            userdata=list()
            subjectData = Subject_Video.objects.get(Subject_Video_Id = subjectid )
            mydata=(Ser_subject(subjectData))
            userdata.append(mydata.data)
            return HttpResponse(json.dumps(userdata))

    except:
        return redirect('/teacherpannel')



##Upload single course video
def uploadsinglevideo(request):
    try:
        if request.method=="POST":
            Trainer_Id=Trainer_Account.objects.get(Trainer_Account_Id=request.session['trainerid'])
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
            return redirect('/teacherpannel/uploadsinglevideo')
        
        
        else:
            Subject=Single_Video.objects.filter(Trainer_Id = request.session['trainerid'] )
            category=Category.objects.all()
            return render(request,'teacher/Upload_Single_Video.html',{'category':category,'subject':Subject})

    except:
        return redirect('/teacherpannel')


###Delete single video
def deletesinglevideo(request,id):
    try:
        data=Single_Video.objects.get(Single_Video_id=id)
        data.delete()
        messages.error(request,"Delete Sucessfully")
        return redirect('/teacherpannel/uploadsinglevideo')

    except:
        return redirect('/teacherpannel')


##Edit single course video
def show_edit_singlevideo(request):

    try:
    
        if request.method == "POST":
            subjid=request.POST['subjid']
            subject=Single_Video.objects.get(Single_Video_id=subjid)
            subject.Category_Id=Category.objects.get(C_Name=request.POST['Category_Id'])
            Title_Name=request.POST['Title_Name']
            Decsription=request.POST['Decsription']
            Difficulty=request.POST['Difficulty']
            Intensity=request.POST['Intensity']
            getsubject = Single_Video.objects.get(Single_Video_id = subjid)
            getsubject.Category_Id = subject.Category_Id
            getsubject.Title_Name = Title_Name
            getsubject.Difficulty = Difficulty
            getsubject.Intensity = Intensity
            getsubject.Decsription = Decsription
            getsubject.save()
            Thumbnail = request.FILES.get('Thumbnail',False)
            Video = request.FILES.get('Video',False)
            
            if Thumbnail:
                getsubject.Thumbnail = Thumbnail
                getsubject.save()
        
            
            if Video:
                getsubject.Video = Video
                getsubject.save()

            
            messages.success(request,"Update Details Sucessfully")
            return redirect('/teacherpannel/uploadsinglevideo')
        
        
        else:
            subjectid = request.GET['id']
            userdata=list()
            subjectData = Single_Video.objects.get(Single_Video_id = subjectid )
            mydata=(Ser_Single_Video(subjectData))
            userdata.append(mydata.data)
            return HttpResponse(json.dumps(userdata))

  
    except:
        return redirect('/teacherpannel')

def logout(request):
    try:
        del request.session['trainerid']
        del request.session['userName']
        del request.session['teacherrole']
        del request.session['teacherusername']
        return redirect('/superadmin/teacherlogin')

    except:
        return redirect('/superadmin/teacherlogin')

