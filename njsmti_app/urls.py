from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='dashboard'),
    path('about/', about, name='about'),
    path('efc/', eco_friendly_campus, name='efc'),
    path('gb/', gb, name='gb'),
    path('classroom/', classroom, name='classroom'),
    path('computerlab/', computerlab, name='computerlab'),
    path('languagelab/', languagelab, name='languagelab'),
    path('library/', library, name='library'),
    path('auditoriumhall/', auditoriumhall, name='auditoriumhall'),

    path('aboutprogramme/', aboutprogramme, name='aboutprogramme'),
    path('directormessege/', dm, name='dm'),
    path('hodmessege/', hod, name='hod'),
    path('academic/', academic, name='academic'),
    path('faculty/', faculty, name='faculty'),
    path('alumni/', alumni, name='alumni'),
    path('expert/', expert, name='expert'),

    path('aboutMCAprogramme/', aboutprogramme1, name='aboutprogramme1'),
    path('MCAhodmessege/', hod1, name='hod1'),
    path('MCAacademic/', academic1, name='academic1'),
    path('MCAfaculty/', faculty1, name='faculty1'),
    path('MCAalumni/', alumni1, name='alumni1'),
    path('MCAexpert/', expert1, name='expert1'),

    path('studentcorner/', studentcorn, name='studentcorner'),
    path('anti-ragging-committe/', commity, name='commity'),
    path('event/', event, name='event'),
    path('galaxy/', galaxy, name='galaxy'),
    path('press/', press, name='press'),
    path('contactus/', contactus, name='contactus'),
    

    path('squery/', squery, name='squery'),

    path('dheader/', Dheader, name='dheader'),
    
    path('reply/<str:email>/<str:qu>', replyuser, name='replyuser'),

    path('fheader/', Fheader, name='fheader'),
    path('diary/', diary, name='diary'),
    

    path('sadmission/', sadmission, name='sadmission'),

    path('addfaculty/', addfaculty, name='addfaculty'),
   
    path('facultydata/', facultydata, name='facultydata'),

    path('diraddfaculty/', diraddfaculty, name='diraddfaculty'),
    path('allfacultydata/', dirfacultydata, name='allfacultydata'),

    path('studentdata/', studentdata, name='studentdata'),

    path('contactdata/', contact_data, name='contactdata'),

    path('querydata/', Query_data, name='querydata'),

    path('replydata/', Reply_data, name='replydata'),

    path('diarydata/', diarydata, name='diarydata'),

    path('mydata/', mydata, name='mydata'),

    path('sdelete/<str:email>/', sdelete, name='sdelete'),

    path('fdelete/<str:email>/', fdelete, name='fdelete'),
    path('fdelete1/<str:email>/', d_fdelete, name='fdelete1'),

    path('approve/<str:email>/', approve, name='approve'),

    path('supdate/<str:email>/', supdate, name='sedit'),

    path('fupdate/<str:email>/', fupdate, name='fedit'),

    path('login/', login, name='login'),

    path('forgot_pwd/', forgot_pwd, name='forgot_pwd'),
   
    path('varify/', varify, name='varify'),
    
    path('change_pwd/', change_pwd, name='change_pwd'),
    
    path('syllabus/', syllabus, name='syllabus'),

    path('scholarship/', scholarship, name='scholarship'),

    path('flogout/', flogout, name='flogout'),

    path('material/', material, name='material'),
    
    path('student/show_material/', show_material, name='show_material'),

    path('slogout/', slogout, name='slogout'),

    path('header1/', lambda request: render(request, 'header1.html'), name='header1'),
    path('header/', lambda request: render(request, 'header.html'), name='header'),
    path('Sheader/', lambda request: render(request, 'Sheader.html'), name='Sheader'),

    path('footer/', lambda request: render(request, 'footer.html'), name='footer'),

    path('dlogout/', dlogout, name='dlogout'),
]