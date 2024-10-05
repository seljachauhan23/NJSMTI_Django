from datetime import timezone
import datetime
import random
from django.shortcuts import redirect, render
from .models import *
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

# from appName.models import *

#send mail function
def SendMail(user_email, Subject, Message):
    send_mail(
        Subject,  # Subject
        Message,  # Message
        'njsmticampus@gmail.com',  # From email
        [user_email],  # To email
    )
    
def clean_data(value):
    """Utility function to clean and convert values."""
    if isinstance(value, tuple) and len(value) > 0:
        return value[0]  # Extract the first element from the tuple
    return value  # Return the value directly if not a tuple
    
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')


def eco_friendly_campus(request):
    return render(request, 'efc.html')

def gb(request):
    return render(request, 'gb.html')


def classroom(request):
    return render(request, 'classroom.html')


def computerlab(request):
    return render(request, 'computerlab.html')

def languagelab(request):
    return render(request, 'languagelab.html')

def library(request):
    return render(request, 'library.html')

def auditoriumhall(request):
    return render(request, 'auditoriumhall.html')

def aboutprogramme(request):
    return render(request, 'aboutprogramme.html')

def dm(request):
    return render(request, 'dm.html')

def hod(request):
    return render(request, 'hod.html')

def academic(request):
    return render(request, 'academic.html')

def faculty(request):
    return render(request, 'faculty.html')

def alumni(request):
    return render(request, 'Alumni.html')

def expert(request):
    return render(request, 'expert.html')

def aboutprogramme1(request):
    return render(request, 'aboutprogramme1.html')

def hod1(request):
    return render(request, 'hod1.html')

def academic1(request):
    return render(request, 'academic1.html')

def faculty1(request):
    return render(request, 'faculty1.html')

def alumni1(request):
    return render(request, 'Alumni1.html')

def expert1(request):
    return render(request, 'expert1.html')

def studentcorn(request):
    return render(request, 'studentcorn.html')

def commity(request):
    return render(request, 'commity.html')

def event(request):
    return render(request, 'event.html')

def galaxy(request):
    return render(request, 'galaxy.html')

def press(request):
    return render(request, 'press.html')

def contactus(request):
    if request.method == "POST":
        contact_data = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            mobile = request.POST.get('ph'),
            message = request.POST.get('msg'),
        )
        try:
            SM = "Message Sent Successfully."
            contact_data.save()
            return render(request, 'contactus.html',{'SM' : SM})
        except:
            return render(request, 'contactus.html')
    return render(request, 'contactus.html')

def contact_data(request):
    contact_data = Contact.objects.all()
    return render(request, 'display_contactus.html', {'data' : contact_data})

def squery(request):
    email = request.session.get('email')
    name = Student.objects.get(email = email)
    if request.method == "POST":
        Query_data = Query(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            query = request.POST.get('ph'),
        )
        
        try:
            SendMail(request.POST.get('email'), 'Query Send Confirmation', 'Your Query is Recieved by Us.')
            SM = "Your Query Sent Successfully.."
            Query_data.save()
            return render(request, 'squery.html', {'SM' : SM})
        except:
            SM = "Please Try Again!!"
            return render(request, 'squery.html', {'SM' : SM})
    return render(request, 'squery.html', {'name' : name})

def Query_data(request):
    try:
        Query_data = Query.objects.all()
        request.session['email'] = Query_data.email
    except Exception as e:
        print(e)
        return render(request, 'querydata.html', {'query' : Query_data})

def Dheader(request):
    return render(request, 'dheader.html')



def replyuser(request, email, qu):
    if request.method == "POST":
        try:
            # Clean the email and query values from the form
            email = clean_data(request.POST.get('email'))
            query = clean_data(request.POST.get('ph'))

            # Create a new ReplyQuery instance with the cleaned data
            reply_data = ReplyQuery(
                email=email,
                question = qu,
                query=query
            )

            # Save the reply_data
            reply_data.save()

            # Filter and delete the corresponding query from the Query model
            Delete_query = Query.objects.filter(email=email, query = qu)
            if Delete_query.exists():
                Delete_query.delete()
            else:
                print(f"No query found with the value: {query}")

            # Prepare the email message
            Message = f"{email}, Greetings from N.J.Sonecha MNG & TECH Institute, Your query has been resolved successfully. Director-K.C Dwivedi."
            
            # Send the email
            SendMail(email, 'Regarding Your Query', Message)

            # Redirect to 'querydata' on success
            return redirect('querydata')

        except Exception as e:
            print(f"An error occurred: {e}")
            # Return to the same page with the email pre-filled in case of an error
            return render(request, 'reply.html', {'email': email})

    # If the request method is GET, render the reply form
    return render(request, 'reply.html', {'email': email, 'qu' : qu})

def Reply_data(request):
    reply = ReplyQuery.objects.all()
    return render(request, 'replydata.html', {'reply': reply})

def Fheader(request):
    return render(request, 'fheader.html')

def diary(request):
    email = request.session.get('email')
    name = AllFaculty.objects.get(email = email)
    name = name.name
    if request.method == "POST":
        diary_data = Diary(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            date = request.POST.get('date'),
            message = request.POST.get('msg'),
            
        )
        
        try:
            diary_data.save()
            SM = "Your diary Written Successfully.."
            return render(request, 'diary.html', {'SM' : SM})
        except:
            SM = "Please Try Again Later.."
            return render(request, 'diary.html', {'SM' : SM})
    return render(request,'diary.html', {'email' : email, 'name' : name})

def diarydata(request):
    diary = Diary.objects.filter(email=request.session.get('email'))
    return render(request, 'diarydata.html', {'diary': diary})

def sadmission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        adr = request.POST.get('adr')
        sph = request.POST.get('sph')
        pph = request.POST.get('pph')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        bp = request.POST.get('bp')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        pwd = request.POST.get('pwd')
        clg = request.POST.get('clg')
        course = request.POST.get('course')
        semester = request.POST.get('sem')
        class_name = request.POST.get('class')
        cgpa = request.POST.get('cgpa')
        
        # Validation
        if not (name and adr and sph and pph and email and dob and bp and category and gender and nationality and pwd and clg and course and cgpa):
            return render(request, 'sadmission.html', {'error': "All fields are required."})

        if len(sph) < 10 or len(pph) < 10:
            return render(request, 'sadmission.html', {'error': "Mobile numbers must be at least 10 digits."})

        if len(pwd) < 8:
            return render(request, 'sadmission.html', {'error': "Password must be at least 8 characters."})
        
        try:
             # Create and save the student
            student = Student(
                name=name,
                address=adr,
                stud_mob=sph,
                parents_mob=pph,
                email=email,
                dob=dob,
                birth_place=bp,
                category=category,
                gender=gender,
                nationality=nationality,
                college=clg,
                course=course,
                semester=semester,
                class_name=class_name,
                cgpa=cgpa,
                password=pwd
            )
            student.save()
            # Sending email
            Message = f'{name} ,Greeting from N.J.Soneca MNG & TECH Institute,Your Admission Preocess Complete Successfully for Other Process Please Contact The Institute With Student Documents.Congratulation Director-K.C Dwivedi.'
            SendMail(email, 'Regrading Your Admission', Message)
            return render(request, 'sadmission.html', {'SM': "Your Registration was Successful. Check Your Mail."})
        except Exception as e:
            print(f"Error saving student: {e}")  # Log the actual error
            return render(request, 'sadmission.html', {'SM': "Your Registration was Unsuccessful Enter Valid Details. Check Your Mail."})
    return render(request, 'sadmission.html')

def studentdata(request):
    search = request.GET.get('search', '')
    students = ''
    if search:
        students = Student.objects.filter(
            models.Q(name__icontains=search) |
            models.Q(email__icontains=search) |
            models.Q(course__icontains=search)
        )
    else:
        students = Student.objects.all()
    
    return render(request, 'studentdata.html', {'students': students, 'search': search})

def mydata(request):
    mydata = Student.objects.filter(email=request.session.get('email'))
    return render(request, 'mydata.html', {'mydata': mydata})

def addfaculty(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        adr = request.POST.get('adr')
        sph = request.POST.get('sph')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        bp = request.POST.get('bp')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        pwd = request.POST.get('pwd')
        course = request.POST.get('course')

        # Validation
        if not (name and adr and sph and email and dob and bp and category and gender and nationality and pwd and course):
            return render(request, 'addfaculty.html', {'error': "All fields are required."})

        if len(sph) < 10 or len(pwd) < 8:
            return render(request, 'addfaculty.html', {'error': "Mobile number must be at least 10 digits and password must be at least 8 characters."})

        # Create and save the faculty
        faculty = Faculty(
            name=name,
            address=adr,
            mobile=sph,
            email=email,
            dob=dob,
            birthplace=bp,
            category=category,
            gender=gender,
            nationality=nationality,
            course=course,
            password=pwd,
            # otp=str(random.randint(100000, 999999))
        )
        try:
            faculty.save()
            return render(request, 'addfaculty.html', {'SM': "Applied Successfully"})
        except:
            return render(request, 'addfaculty.html', {'SM': "Applied Unsuccessfully"})
    return render(request, 'addfaculty.html')
    
def diraddfaculty(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        adr = request.POST.get('adr')
        sph = request.POST.get('sph')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        bp = request.POST.get('bp')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        pwd = request.POST.get('pwd')
        course = request.POST.get('course')

        # Validation
        if not (name and adr and sph and email and dob and bp and category and gender and nationality and pwd and course):
            return render(request, 'dir_add_faculty.html', {'error': "All fields are required."})

        if len(sph) < 10 or len(pwd) < 8:
            return render(request, 'dir_add_faculty.html', {'error': "Mobile number must be at least 10 digits and password must be at least 8 characters."})

        # Create and save the faculty
        faculty = AllFaculty(
            name=name,
            address=adr,
            mobile=sph,
            email=email,
            dob=dob,
            birthplace=bp,
            category=category,
            gender=gender,
            nationality=nationality,
            course=course,
            password=pwd,
        )
        try:
            faculty.save()
            return render(request, 'dir_add_faculty.html', {'SM': "Add Faculty Successfully"})
        except:
            return render(request, 'dir_add_faculty.html', {'SM': "Add Faculty Unsuccessfully"})
    return render(request, 'dir_add_faculty.html')

def facultydata(request):
    faculty = Faculty.objects.all()
    return render(request, 'facultydata.html', {'faculty': faculty})

def dirfacultydata(request):
    search = request.GET.get('search', '')
    if search:
        faculty = AllFaculty.objects.filter(
            models.Q(name__icontains=search) |
            models.Q(email__icontains=search) |
            models.Q(course__icontains=search)
        )
    else:
        faculty = AllFaculty.objects.all()
    
    return render(request, 'allfacultydata.html', {'faculty': faculty, 'search': search})


def sdelete(request,email):
    student = Student.objects.get(email= email)
    if student:
        student.delete()
        return redirect('studentdata')
    return render(request, 'studentdata.html')


def fdelete(request,email):
    try:
        faculty = AllFaculty.objects.get(email= email)
        name = faculty.name
        faculty.delete()
        Message = f'{name} ,Your Account is deleted.'
        SendMail(email, 'Regrading to Account Delete', Message)
        return redirect('facultydata')
    except:
        return redirect('facultydata')

def d_fdelete(request,email):
    faculty = Faculty.objects.get(email = email)
    if faculty:
        email = faculty.email
        faculty_temp= Faculty.objects.get(email = email)
        if faculty_temp.delete():
            Message =f"{faculty.name} ,We are Sorry to not hiring to you as a professior but if we require more staff we contact you first,Thank You. Director-K.C.Dwivedi"
            SendMail(email, 'Regarding Your Job Application', Message)
            pass
    return render(request, 'facultydata.html')

def approve(request, email):
    try:
        faculty = Faculty.objects.get(email = email)
        faculty1 = AllFaculty(
        name = faculty.name,
        address = faculty.address,
        mobile = faculty.mobile,
        email = faculty.email,
        dob = faculty.dob,
        birthplace = faculty.birthplace,
        category = faculty.category,
        gender = faculty.gender,
        nationality = faculty.nationality,
        course = faculty.course,
        password = faculty.password    
            
        )
        faculty1.save()
        Message = f'{faculty.name} ,Greeting from N.J.Soneca MNG & TECH Institute,Congratulations to Being a Part of NJSMTI as a Assistance Proffessor Please Joining into maximum 10 Days with your Documents if You not want to join then inform us.Thank You. Director-K.C.Dwivedi'
        SendMail(faculty.email, 'Regarding Your Job Application', Message)
        faculty.delete()
        faculty = Faculty.objects.all()
        return render(request, 'facultydata.html', {'faculty' : faculty})
    except:
        return render(request, 'facultydata.html', {'SM' : "Please Try Again Later.."})
    return render(request, 'allfacultydata.html')

def supdate(request, email):
    student = Student.objects.get(email = email)
    if request.method == "POST":
 
        name = request.POST.get('name')
        address = request.POST.get('adr')
        student_mobile = request.POST.get('sph')
        parent_mobile = request.POST.get('pph')
        email = request.POST.get('email')
        birthplace = request.POST.get('bp')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        class_name = request.POST.get('class_name')
        cgpa = request.POST.get('cgpa')
        course = request.POST.get('course')
        semester = request.POST.get('semester')
        pwd = request.POST.get('pwd')
        
                     
        try:
            student.name = clean_data(name);
            student.address = clean_data(address);
            student.stud_mob = clean_data(student_mobile);
            student.parents_mob = clean_data(parent_mobile);
            student.email = clean_data(email);
            student.birth_place = clean_data(birthplace);
            student.category = clean_data(category);
            student.gender = clean_data(gender);
            student.nationality = clean_data(nationality);
            student.class_name = clean_data(class_name);
            student.cgpa = clean_data(cgpa);
            student.course = clean_data(course);
            student.semester = clean_data(semester);
            student.password = clean_data(pwd);
            student.save()
            return redirect('studentdata')
        except Exception as e:
            print(e)
            return render(request,'studentdata.html')
    return render(request, 'sedit.html', {'student' : student})


def fupdate(request,email):
    allfaculty = AllFaculty.objects.get(email = email)
    
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('adr')
        mobile = request.POST.get('sph')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        birthplace = request.POST.get('bp')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        course = request.POST.get('course')
        pwd = request.POST.get('pwd')
        
        try:
            allfaculty = AllFaculty.objects.get(email = email)
            allfaculty.name = clean_data(name)
            allfaculty.address = clean_data(address)
            allfaculty.mobile = clean_data(mobile)
            allfaculty.dob = clean_data(dob)
            allfaculty.birthplace = clean_data(birthplace)
            allfaculty.category = clean_data(category)
            allfaculty.gender = clean_data(gender)
            allfaculty.nationality = clean_data(nationality)
            allfaculty.course = clean_data(course)
            allfaculty.password = clean_data(pwd)
            
            allfaculty.save()
            return redirect('allfacultydata')
        
        except Exception as e:
            print(e)
             # Sending email
            Message = f'{name} ,Your information is updated successfully by director.'
            SendMail(email, 'Regrading Your Information Update', Message)
            return redirect('allfacultydata')
        
    return render(request,'fedit.html', {'allfaculty' : allfaculty})

def material(request):
    if request.method == "POST":
        material = Material(
            semester = request.POST.get('semester'),
            link = request.POST.get('material_path'),
            Topic = request.POST.get('topic')
        )
        
        try:
            material.save()
            return render(request, "study_meterial.html", {'SM' : "Your Material Upload Successfully.."})
        
        except:
            return render(request, "study_meterial.html", {'SM' : "OOps Some Error Occurs.."})
        
    return render(request, 'study_meterial.html')

def show_material(request):
    email = request.session.get('email')
    
    try:
        student = Student.objects.get(email = email)
        if student:
            material = Material.objects.filter(semester = student.semester)
            return render(request, 'show_material.html',{'material': material})
        
    except Exception as e:
        print(e)
        return render(request, 'show_material.html',{'SM' : "Oops No Material found.."})
    return render(request, 'show_material.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        role = request.POST.get('role')
        
        if role == 'Director':
            director = ''
            try:
                director = Director.objects.get(email=email, password=pwd)
            except:
                pass
            if director is None:
                return render(request,'login.html', {'SM' : "Enter valid data.."})
            if role:
                request.session['email']= email
                request.session['role'] = role
                
                return render(request,'dheader.html')
        elif role == 'Faculty':
            faculty = ''
            try:
                faculty = AllFaculty.objects.get(email=email, password=pwd)
            except:
                pass
            if faculty is None:
                return render(request,'login.html', {'SM' : "Enter valid data.."})
            if role:
                request.session['email']= email
                request.session['role'] = role
                
                return render(request,'fheader.html')
        else:
            student = ''
            try:
                student = Student.objects.get(email=email, password=pwd)
            except:
                pass
            if student is None:
                return render(request,'login.html', {'SM' : "Enter valid data.."})
            if role:
                request.session['email']= email
                request.session['role'] = role
                
                return render(request,'sheader.html')
    return render(request, 'login.html')

def forgot_pwd(request):
    if request.method == "POST":
        email = request.POST.get('email')
        role = request.POST.get('role')
        
        if role == 'Director':
            director = ''
            try:
                director = Director.objects.get(email = email)
            except: 
                pass
            if director:
                otp = random.randint(100000,999999)
                
                request.session['email'] = email
                request.session['otp'] = otp
                request.session['role'] = role
                Message = f'{email} Your Forgot Password OTP is : {otp}'
                SendMail(email, 'forgot Password', Message)
                return render(request, 'varify.html')
            else:
                return render(request, 'forgot_pwd.html',{'SM' : "select valid role."})
        elif role == 'Faculty':
            faculty = ''
            try:
                faculty = AllFaculty.objects.get(email = email)
            except:
                pass
            if faculty:
                otp = random.randint(100000,999999)
                
                request.session['email'] = email
                request.session['otp'] = otp
                request.session['role'] = role
                
                #email
                Message = f'{email} Your Forgot Password OTP is : {otp}'
                SendMail(email, 'forgot Password', Message)
                
                return render(request, 'varify.html')
            else:
                return render(request, 'forgot_pwd.html',{'SM' : "select valid role."})
            
        else:
            student = ''
            try:
                student = Student.objects.get(email = email)
            except:
                pass
            if student:
                otp = random.randint(100000,999999)
                
                request.session['email'] = email
                request.session['otp'] = otp
                request.session['role'] = role
                
                #email
                Message = f'{email} Your Forgot Password OTP is : {otp}'
                SendMail(email, 'forgot Password', Message)
                return redirect('varify')
            else:
                return render(request, 'forgot_pwd.html',{'SM' : "select valid role."})
    return render(request, 'forgot_pwd.html')


def varify(request):
    email = request.session.get('email')
    otp = str(request.session.get('otp'))   
    role = request.session.get('role')
    print(role)
    
    if request.method == "POST":
        # email = request.POST.get('email')
        otp1 = str(request.POST.get('otp'))     
        
        if role == 'Director':
            try:
                director = Director.objects.get(email = email)

                if director:
                    if otp1 == otp:
                        return redirect('change_pwd') 
            except:
                return render(request, 'varify.html', {'SM' : "Please enter valid otp"})
        elif role == 'Faculty':
            try:
                faculty = AllFaculty.objects.get(email = email)

                if faculty:
                    if otp1 == otp:
                        return redirect('change_pwd') 
            except:
                return render(request, 'varify.html', {'SM' : "Please enter valid otp"})
        else:
            try:
                student = Student.objects.get(email = email)

                if student:
                    if otp1 == otp:
                        return redirect('change_pwd') 
            except:
                return render(request, 'varify.html', {'SM' : "Please enter valid otp"})
    return render(request,'varify.html')

def change_pwd(request):
    role = request.session.get('role')
    email = request.session.get('email')
    print(role, email)
    
    if request.method =="POST":
        password = request.POST.get('password')
    
        if role == 'Director':
            try:
                director = Director.objects.get(email = email)
                director.password = password
                director.save()
                #email
                Message = f'{email} Your Password Changed Successfully.'
                SendMail(email, 'Update Password', Message)
                request.session.flush()
                return render(request, 'login.html', {'SM' : 'your password changed successfully.'})
            except Exception as e:
                print(e)
                return render(request, 'change_pwd.html', {'SM' : 'invalid credentials.'})
            
        elif role == 'Faculty':
            
            try:
                faculty = AllFaculty.objects.get(email = email)
                faculty.password = password
                faculty.save()
                #email
                Message = f'{email} Your Password Changed Successfully.'
                SendMail(email, 'Update Password', Message)
                request.session.flush()
                return render(request, 'login.html', {'SM' : 'your password changed successfully.'})
            except Exception as e:
                print(e)
                return render(request, 'change_pwd.html', {'SM' : 'invalid credentials.'})
        if role == 'Student':
            
            try:
                student = Student.objects.get(email = email)
                student.password = password
                student.save()
                #email
                Message = f'{email} Your Password Changed Successfully.'
                SendMail(email, 'Update Password', Message)
                request.session.flush()
                return render(request, 'login.html', {'SM' : 'your password changed successfully.'})
            except Exception as e:
                print(e)
                return render(request, 'change_pwd.html', {'SM' : 'invalid credentials.'})
    return render(request, 'change_pwd.html')

def syllabus(request):
    return render(request, 'syllabus.html')

def scholarship(request):
    return render(request, 'scholarship.html')

def flogout(request):
    request.session.flush()
    return redirect('/login')

def slogout(request):
    request.session.flush()
    return redirect('/login')

def dlogout(request):
    request.session.flush()
    return redirect('/login')