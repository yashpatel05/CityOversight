from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from CityWebsite.models import User_Signup,User_Role,User_Complain,Camera_Circle,Camera_City,Camera_Name,Camera_State,Report_Details
from CityWebsite.forms import UserRoleForm, CameraStateForm, CameraCityForm, CameraCircleForm, CameraInfoForm, \
    UserSignupForm, EditUserSignupForm, EditUserProfileForm, NewReportForm
from CityWebsite.functions import handle_uploaded_file_photo,handle_captured_image

import sys
from datetime import datetime

# Create your views here.


def index(request):
    if request.session.has_key('id'):
        user_data = User_Signup.objects.filter(user_status=0).select_related("role")
        garbage_report = Report_Details.objects.filter(report_status=0)
        complain_data = User_Complain.objects.filter(complain_status=0)
        camera_data = Camera_Name.objects.filter(camera_status=0).select_related("circle")
        user_count = User_Signup.objects.all().count()
        garbage_report_count = Report_Details.objects.all().count()
        complain_count = User_Complain.objects.all().count()
        camera_count = Camera_Name.objects.all().count()
        complain_pending_count = User_Complain.objects.filter(complain_status=0).count()
        report_pending_count = Report_Details.objects.filter(report_status=0).count()
        user_pending_count = User_Signup.objects.filter(user_status=0).count()
        camera_pending_count = Camera_Name.objects.filter(camera_status=0).count()
        return render(request, "index_employee.html", {'user': user_data, 'report': garbage_report, 'complain': complain_data, 'camera': camera_data,
                                              'user_count': user_count, 'report_count': garbage_report_count, 'camera_count': camera_count,
                                              'complain_count': complain_count, 'complain_pending_count': complain_pending_count,
                                              'report_pending_count': report_pending_count, 'user_pending_count': user_pending_count,
                                              'camera_pending_count': camera_pending_count})
    return render(request, "login.html")


def logout(request):
    if request.session.has_key('id'):
        try:
            del request.session['id']
            del request.session['first_name']
            del request.session['role']
            del request.session['photo']
        except:
            pass
        return HttpResponseRedirect("/login")
    return render(request, 'login.html')


def profile(request):
    if request.session.has_key('id'):
        id = request.session['id']
        print("-------", id)
        user_data = User_Signup.objects.get(user_id=id)
        print("----------", user_data.first_name)
        return render(request, "profile_employee.html", {'user': user_data})
    return render(request, "login.html")


def camera_select_show(request):
    state = Camera_State.objects.all()

    if request.session.has_key('id'):
        if request.method=="POST":
            print("--------")
        return render(request, 'camera_select_show_employee.html', {'state': state})
    return render(request, 'login.html')


def captured_image(request):
    if request.session.has_key('id'):
        return render(request, 'captured_image_show_employee.html')
    return render(request, 'login.html')


def scanned_image(request):
    if request.session.has_key('id'):
        if request.method=="POST":
            form = NewReportForm(request.POST, request.FILES)
            print("----------", form.errors)
            if form.is_valid():
                try:
                    handle_captured_image(request.FILES['captured_image'])
                    #form.save()
                    return render(request, 'scanned_image_show_employee.html',)

                except:
                    pass
                    print("------ Error -----", sys.exc_info())

        else:
            form = NewReportForm()
            return render(request, 'captured_image_show_employee.html',
                          {'form': form})

    return render(request, 'login.html')


def generate_report(request):
    if request.session.has_key('id'):
        if request.method=="POST":
            print("-----------Generated Report----------")

        return render(request, 'generate_report_show_employee.html')
    return render(request, 'login.html')


def garbage_report_show(request):
    if request.session.has_key('id'):
        garbage_report = Report_Details.objects.all()
        return render(request, "show_garbage_report_employee.html", {'report': garbage_report})
    return render(request, 'login.html')


def complain_data_show(request):
    if request.session.has_key('id'):
        complain_data = User_Complain.objects.all()
        return render(request, "show_complain_data_employee.html", {'complain': complain_data})
    return render(request, 'login.html')


def update_user_profile_show(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        return render(request, 'update_user_profile_employee.html', {'user': user_data})
    return render(request, "login.html")


def edit_user_profile(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        form =  EditUserSignupForm(request.POST, instance=user_data)
        print("------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/employee/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_employee.html', {'user': user_data})
    return render(request, 'login.html')


def edit_user_profile_photo(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        form =  EditUserProfileForm(request.POST, request.FILES , instance=user_data)
        print("------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file_photo(request.FILES['profile_photo'])
                form.save()
                user = User_Signup.objects.get(user_id=id)
                request.session.modified = True
                request.session['photo'] = user.profile_photo
                return redirect("/employee/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_employee.html', {'user': user_data})
    return render(request, 'login.html')


def remove_user_profile_photo(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        user_data.profile_photo="blank_user.png"
        user_data.save()

        user = User_Signup.objects.get(user_id=id)
        request.session.modified = True
        request.session['photo'] = user.profile_photo
        return redirect("/employee/index")

    return render(request, 'login.html')


def accept_user_signup(request, id):
    if request.session.has_key('id'):
        user_data = User_Signup.objects.get(user_id=id)
        user_data.user_status=1
        user_data.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def accept_camera(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status=1
        camera.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def accept_garbage_report(request, id):
    if request.session.has_key('id'):
        report = Report_Details.objects.get(report_id=id)
        report.report_status=1
        report.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def accept_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        complain.complain_status=1
        complain.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def reject_user_signup(request, id):
    if request.session.has_key('id'):
        user_data = User_Signup.objects.get(user_id=id)
        user_data.user_status=2
        user_data.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def reject_camera(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status=2
        camera.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def reject_garbage_report(request, id):
    if request.session.has_key('id'):
        report = Report_Details.objects.get(report_id=id)
        report.report_status=2
        report.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def reject_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        complain.complain_status=2
        complain.deduction_points=10
        uid = complain.user_id
        complain.save()
        user = User_Signup.objects.get(user_id=uid)
        user.complain_points = user.complain_points - 10
        user.save()
        return HttpResponseRedirect('/employee/index')
    return render(request, 'login.html')


def solved_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        complain.complain_status = 3
        complain.solved_date = datetime.now()
        complain.save()
        return HttpResponseRedirect('/employee/complain')
    return render(request, 'login.html')


def solved_garbage(request, id):
    if request.session.has_key('id'):
        report = Report_Details.objects.get(report_id=id)
        report.report_status = 3
        report.save()
        return HttpResponseRedirect('/employee/report')
    return render(request, 'login.html')


def load_city(request):
    if request.session.has_key('id'):
        sid = request.GET.get('state')
        print("--------++++++++++++-----------",sid)
        city = Camera_City.objects.filter(state_id=sid)
        return render(request, 'load_city_employee.html', {'city': city})
    return render(request, 'login.html')


def load_circle(request):
    if request.session.has_key('id'):
        cid = request.GET.get('city')
        print("--------++++++++++++-----------",cid)
        circle = Camera_Circle.objects.filter(city_id=cid)
        return render(request, 'load_circle_employee.html', {'circle': circle})
    return render(request, 'login.html')


def load_camera(request):
    if request.session.has_key('id'):
        crid = request.GET.get('circle')
        print("--------++++++++++++-----------",crid)
        camera = Camera_Name.objects.filter(circle_id=crid,camera_status=1)
        return render(request, 'load_camera_employee.html', {'camera': camera})
    return render(request, 'login.html')