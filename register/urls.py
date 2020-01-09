from django.urls import path
from register import views
from django.views.generic import TemplateView
urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),

    path('admin/',TemplateView.as_view(template_name='admin.html'),name='admin'),
    path('addfaculty/',TemplateView.as_view(template_name='addfaculty.html'),name='addfaculty'),
    
    path('index',views.authentication,name='submit'),
    path('addfaculty/',views.addfaculty,name='addfaculty'),
    path('facultyregistartion/',TemplateView.as_view(template_name='faculty.html'),name='faculty'),
    
    path('studentregistartion/',TemplateView.as_view(template_name='studentregistration.html'),name='studentregistration'),
    path('facultysignup/',views.facultysign,name='facultysignup'),
    path('studentsignup/',views.signupstud,name='studregistration'),
    path('studattendn/',views.studattend,name='studentattendance'),
    path('factapp/',views.facultyleave,name='factapplyleave'),
    path('studapp/',views.studentleave,name='studapplyleave'),
    path('studentmark/',views.stdmark,name='studmark'),
    path('pass/',TemplateView.as_view(template_name='password.html'),name='password'),
    path('mob/',TemplateView.as_view(template_name='mobile.html'),name='mobile'),
    path('em/',TemplateView.as_view(template_name='email.html'),name='email'),
    path('mydetails/',TemplateView.as_view(template_name='personaldetails.html'),name='personaldetails'),
    path('details/',views.detailsstudent,name='personaldetails'),
    path('mymarks/',TemplateView.as_view(template_name='viewmark.html'),name='viewmark'),
    path('markdetails/',views.markview,name='viewmark'),
    path('myattendence/',TemplateView.as_view(template_name='viewattend.html'),name='viewattend'),
    path('attendencedetails/',views.attendview,name='viewattend'),
    path('myfac/',TemplateView.as_view(template_name='viewfac.html'),name='viewfac'),
    path('facdetails/',views.facview,name='viewfac'),
    path('mystud/',TemplateView.as_view(template_name='viewstd.html'),name='viewstd'),
    path('studentdetails/',views.studview,name='viewstd'),
    path('',TemplateView.as_view(template_name='logout.html'),name='logout')


    
]
