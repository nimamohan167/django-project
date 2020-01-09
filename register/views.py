from django.shortcuts import render
from django.shortcuts import HttpResponse
from register.models import admin,faculty,facultysignup,student,studentattend,factleave,studleave,studentmark,facultyattendence
from django.http import HttpResponse


def authentication(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username,password=password)
        
        if u.count()==1:
            return render(request,'admin.html')
        else:
            u=faculty.objects.filter(name=username,password=password)
            if u.count()==1:
                return render(request,'factpage.html')
            else:
                u=student.objects.filter(name=username,password=password)
                if u.count()==1:
                     request.session['usernm']=username
                     qry=student.objects.all().filter(name=username)[0]
                     request.session['stid']=qry.stdid
                     return render(request,'studentpage.html')
                else:
                    return HttpResponse('login unsuccesful')    
        
                 
def facultysign(request):
    if request.method=='POST':
        factid = request.POST.get('factid')
        name =request.POST.get('name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        gender =request.POST.get('gender')
        qualification =request.POST.get('qualification')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        assbatch= request.POST.get('assbatch') 
        c=facultysignup(factid=factid,name=name,address=address,dob=dob,gender=gender,qualification=qualification,mobile=mobile,
        email=email,password=password,assbatch=assbatch)  
        c.save()
    return render(request,'faculty.html')              

def addfaculty(request):
    if request.method =='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        
        b=faculty(name=name,password=password)
        b.save()
    return render(request,'addfaculty.html')
def signupstud(request):
    if request.method =='POST':
        stdid=request.POST.get('stdid')
        admno=request.POST.get('admno')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        admdate=request.POST.get('admdate')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')

        d=student(stdid=stdid,admno=admno,name=name,address=address,dob=dob,gender=gender,mobile=mobile,admdate=admdate,guardian=guardian,batch=batch,email=email,password=password)
        d.save()
    return render(request,'studentregistration.html')
def studattend(request):
    if request.method=='POST':
        date = request.POST.get('date')
        stdid = request.POST.get('stdid')
        name = request.POST.get('name')
        hour1status = request.POST.get('hour1status')
        hour2status = request.POST.get('hour2status')
        hour3status = request.POST.get('hour3status')
        hour4status = request.POST.get('hour4status')

        e=studentattend(date=date,stdid=stdid,name=name,hour1status=hour1status,hour2status=hour2status,hour3status=hour3status,hour4status=hour4status)    
        e.save()
    return render(request,'studentattendance.html')
def facultyleave(request):
    if request.method=='POST':
        name=request.POST.get('name')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        f=factleave(name=name,fromdate=fromdate,todate=todate,reason=reason)
        f.save()
    return render(request,'factapplyleave.html')    
def studentleave(request):
    if request.method=='POST':
        name=request.POST.get('name')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        g=studleave(name=name,fromdate=fromdate,todate=todate,reason=reason)
        g.save()
    return render(request,'studapplyleave.html')    
def stdmark(request):
    if request.method=='POST':
        stdid= request.POST.get('stdid')
        name =  request.POST.get('name')
        assessmentno =request.POST.get('assessmentno')
        sub1mark =request.POST.get('sub1mark')
        sub2mark =request.POST.get('sub2mark')
        sub3mark =request.POST.get('sub3mark')
        percentage=request.POST.get('percentage')
        h=studentmark(stdid=stdid,name=name,assessmentno=assessmentno,sub1mark=sub1mark,sub2mark=sub2mark,sub3mark=sub3mark,percentage=percentage)
        h.save()
    return render(request,'studmark.html')   

    return render(request,'facultyattendance.html')     
def detailsstudent(request):
    queryset=student.objects.all().filter(name=request.session['usernm'])
    return render(request,'personaldetails.html',{'authors':queryset})
def markview(request):
    querysett=studentmark.objects.all().filter(stdid=request.session['stid'])
    return render(request,'viewmark.html',{'authorss':querysett})
def attendview(request):
    querysettt=studentattend.objects.all().filter(stdid=request.session['stid'])
    return render(request,'viewattend.html',{'authorsss':querysettt}) 
def facview(request):
    querysetttt=facultysignup.objects.all().filter()
    return render(request,'viewfac.html',{'authorssss':querysetttt})
def studview(request):
    querysettttt=student.objects.all().filter()
    return render(request,'viewstd.html',{'authorsssss':querysettttt})


 
# Create your views here.
