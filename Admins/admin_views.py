from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from CityWebsite.models import User_Signup,User_Role,User_Complain,Camera_Circle,Camera_City,Camera_Name,Camera_State,Report_Details
from CityWebsite.forms import UserRoleForm, CameraStateForm, CameraCityForm, CameraCircleForm, CameraInfoForm, \
    UserSignupForm, EditUserSignupForm, EditUserProfileForm
from CityWebsite.functions import handle_uploaded_file_photo
from django.conf import settings
from django.db.models import Q
import sys
import random
from django.contrib import messages
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
        return render(request, "index_admin.html", {'user': user_data, 'report': garbage_report, 'complain': complain_data, 'camera': camera_data,
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
        return render(request, "profile_admin.html", {'user': user_data})
    return render(request, "login.html")


def user_signup_show(request):
    if request.session.has_key('id'):
        user_data = User_Signup.objects.filter(~Q(role = 1)).select_related("role")
        return render(request, "show_user_signup_admin.html", {'user': user_data})
    return render (request, "login.html")


def user_role_show(request):
    if request.session.has_key('id'):
        user_role = User_Role.objects.all()
        return render(request, "show_user_role_admin.html", {'user': user_role})
    return render(request, 'login.html')


def camera_state_show(request):
    if request.session.has_key('id'):
        camera_state = Camera_State.objects.all()
        return render(request, "show_camera_state_admin.html", {'state': camera_state})
    return render(request, 'login.html')


def camera_city_show(request):
    if request.session.has_key('id'):
        camera_city = Camera_City.objects.all().select_related("state")
        return render(request, "show_camera_city_admin.html", {'city': camera_city})
    return render(request, 'login.html')


def camera_circle_show(request):
    if request.session.has_key('id'):
        camera_circle = Camera_Circle.objects.all().select_related("city")
        return render(request, "show_camera_circle_admin.html", {'circle': camera_circle})
    return render(request, 'login.html')


def camera_data_show(request):
    if request.session.has_key('id'):
        camera_data = Camera_Name.objects.all().select_related("circle")
        return render(request, "show_camera_info_admin.html", {'camera': camera_data})
    return render(request, 'login.html')


def garbage_report_show(request):
    if request.session.has_key('id'):
        garbage_report = Report_Details.objects.all()
        return render(request, "show_garbage_report_admin.html", {'report': garbage_report})
    return render(request, 'login.html')


def complain_data_show(request):
    if request.session.has_key('id'):
        complain_data = User_Complain.objects.all()
        return render(request, "show_complain_data_admin.html", {'complain': complain_data})
    return render(request, 'login.html')


def camera_state_delete(request, id):
    if request.session.has_key('id'):
        camera_state=Camera_State.objects.get(state_id=id)
        camera_state.delete()
        return redirect("/admin/state")
    return render(request, 'login.html')


def camera_city_delete(request, id):
    if request.session.has_key('id'):
        camera_city = Camera_City.objects.get(city_id=id)
        camera_city.delete()
        return redirect("/admin/city")
    return render(request, 'login.html')


def camera_circle_delete(request, id):
    if request.session.has_key('id'):
        camera_circle = Camera_Circle.objects.get(circle_id=id)
        camera_circle.delete()
        return redirect("/admin/circle")
    return render(request, 'login.html')


def camera_delete(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.delete()
        return redirect("/admin/camera")
    return render(request, 'login.html')


def insert_camera_state(request):
    if request.session.has_key('id'):
        if request.method=="POST":
            form = CameraStateForm(request.POST)
            print("----------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/admin/state')
                except:
                    pass
        else:
            form = CameraStateForm()

        return render(request, 'insert_camera_state_admin.html', {'form': form})
    return render(request, 'login.html')


def insert_camera_city(request):
    state = Camera_State.objects.all()
    if request.session.has_key('id'):
        if request.method=="POST":
            form = CameraCityForm(request.POST)
            print("----------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/admin/city')
                except:
                    pass
        else:
            form = CameraCityForm()

        return render(request, 'insert_camera_city_admin.html', {'form': form, 'state': state})
    return render(request, 'login.html')


def insert_camera_circle(request):
    state = Camera_State.objects.all()
    if request.session.has_key('id'):
        if request.method=="POST":
            form = CameraCircleForm(request.POST)
            print("----------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/admin/circle')
                except:
                    pass
        else:
            form = CameraCircleForm()

        return render(request, 'insert_camera_circle_admin.html', {'form': form, 'state': state})
    return render(request, 'login.html')


def insert_camera_info(request):
    state = Camera_State.objects.all()
    if request.session.has_key('id'):
        if request.method=="POST":
            form = CameraInfoForm(request.POST)
            print("----------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/admin/camera')
                except:
                    pass
        else:
            form = CameraInfoForm()

        return render(request, 'insert_camera_info_admin.html', {'form': form, 'state': state})
    return render(request, 'login.html')


def update_camera_state_show(request, id):
    if request.session.has_key('id'):
        camera_state = Camera_State.objects.get(state_id=id)
        return render(request, 'update_camera_state_admin.html', {'state': camera_state})
    return render(request, 'login.html')


def update_camera_city_show(request, id):
    state = Camera_State.objects.all()
    if request.session.has_key('id'):
        camera_city = Camera_City.objects.get(city_id=id)
        return render(request, 'update_camera_city_admin.html', {'city': camera_city, 'state': state})
    return render(request, 'login.html')


def update_camera_circle_show(request, id):
    city = Camera_City.objects.all()
    if request.session.has_key('id'):
        camera_circle = Camera_Circle.objects.get(circle_id=id)
        return render(request, 'update_camera_circle_admin.html', {'circle': camera_circle, 'city': city})
    return render(request, 'login.html')


def update_camera_info_show(request, id):
    circle = Camera_Circle.objects.all()
    if request.session.has_key('id'):
        camera_name = Camera_Name.objects.get(camera_id=id)
        return render(request, 'update_camera_info_admin.html', {'camera': camera_name, 'circle': circle})
    return render(request, 'login.html')


def update_user_profile_show(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        return render(request, 'update_user_profile_admin.html', {'user': user_data})
    return render(request, "login.html")


def edit_camera_state(request, id):
    if request.session.has_key('id'):
        camera_state = Camera_State.objects.get(state_id=id)
        form =  CameraStateForm(request.POST, instance=camera_state)
        print("------", form.errors)
        if form.is_valid():
            form.save()
            return redirect("/admin/state")
        return render(request, 'update_camera_state_admin.html', {'state': camera_state})
    return render(request, 'login.html')


def edit_camera_city(request, id):
    if request.session.has_key('id'):
        camera_city = Camera_City.objects.get(city_id=id)
        form =  CameraCityForm(request.POST, instance=camera_city)
        print("------", form.errors)
        if form.is_valid():
            form.save()
            return redirect("/admin/city")
        return render(request, 'update_camera_city_admin.html', {'city': camera_city})
    return render(request, 'login.html')


def edit_camera_circle(request, id):
    if request.session.has_key('id'):
        camera_circle = Camera_Circle.objects.get(circle_id=id)
        form =  CameraCircleForm(request.POST, instance=camera_circle)
        print("------", form.errors)
        if form.is_valid():
            form.save()
            return redirect("/admin/circle")
        return render(request, 'update_camera_circle_admin.html', {'circle': camera_circle})
    return render(request, 'login.html')


def edit_camera_info(request, id):
    if request.session.has_key('id'):
        camera_name = Camera_Name.objects.get(camera_id=id)
        form =  CameraInfoForm(request.POST, instance=camera_name)
        print("------", form.errors)
        if form.is_valid():
            form.save()
            return redirect("/admin/camera")
        return render(request, 'update_camera_info_admin.html', {'camera': camera_name})
    return render(request, 'login.html')


def edit_user_profile(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        form =  EditUserSignupForm(request.POST, instance=user_data)
        print("------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/admin/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_admin.html', {'user': user_data})
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

                return redirect("/admin/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_admin.html', {'user': user_data})
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
        return redirect("/admin/index")

    return render(request, 'login.html')


def accept_user_signup(request, id):
    if request.session.has_key('id'):
        user_data = User_Signup.objects.get(user_id=id)
        user_data.user_status=1
        user_data.save()
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def accept_camera(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status=1
        camera.save()
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def accept_garbage_report(request, id):
    if request.session.has_key('id'):
        report = Report_Details.objects.get(report_id=id)
        report.report_status=1
        report.save()
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def accept_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        complain.complain_status=1
        complain.save()
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def reject_user_signup(request, id):
    if request.session.has_key('id'):
        user_data = User_Signup.objects.get(user_id=id)
        user_data.user_status=2
        user_data.save()
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def reject_camera(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status=2
        camera.save()
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def reject_garbage_report(request, id):
    if request.session.has_key('id'):
        report = Report_Details.objects.get(report_id=id)
        report.report_status=2
        report.save()
        return HttpResponseRedirect('/admin/index')
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
        return HttpResponseRedirect('/admin/index')
    return render(request, 'login.html')


def solved_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        complain.complain_status = 3
        complain.solved_date = datetime.now()
        complain.save()
        return HttpResponseRedirect('/admin/complain')
    return render(request, 'login.html')


def solved_garbage(request, id):
    if request.session.has_key('id'):
        report = Report_Details.objects.get(report_id=id)
        report.report_status = 3
        report.save()
        return HttpResponseRedirect('/admin/report')
    return render(request, 'login.html')


def change_user_status(request, id):
    if request.session.has_key('id'):
        user = User_Signup.objects.get(user_id=id)
        user.user_status = 0
        user.save()
        return HttpResponseRedirect('/admin/user_signup')
    return render(request, 'login.html')


def change_camera_status(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status = 0
        camera.save()
        return HttpResponseRedirect('/admin/camera')
    return render(request, 'login.html')


def load_city(request):
    if request.session.has_key('id'):
        sid = request.GET.get('state')
        print("--------++++++++++++-----------",sid)
        city = Camera_City.objects.filter(state_id=sid)
        return render(request, 'load_city_admin.html', {'city': city})
    return render(request, 'login.html')

def load_circle(request):
    if request.session.has_key('id'):
        cid = request.GET.get('city')
        print("--------++++++++++++-----------",cid)
        circle = Camera_Circle.objects.filter(city_id=cid)
        return render(request, 'load_circle_employee_admin.html', {'circle': circle})
    return render(request, 'login.html')
