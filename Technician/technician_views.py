from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from CityWebsite.models import User_Signup,User_Role,User_Complain,Camera_Circle,Camera_City,Camera_Name,Camera_State,Report_Details
from CityWebsite.forms import UserRoleForm, CameraStateForm, CameraCityForm, CameraCircleForm, CameraInfoForm, \
    UserSignupForm, EditUserSignupForm, EditUserProfileForm
from CityWebsite.functions import handle_uploaded_file_photo
import sys

# Create your views here.


def index(request):
    if request.session.has_key('id'):
        camera_pending_data = Camera_Name.objects.filter(camera_status=0).select_related("circle")
        camera_active_count = Camera_Name.objects.filter(camera_status=1).count()
        camera_pending_count = Camera_Name.objects.filter(camera_status=0).count()

        return render(request, "index_technician.html", {'camera': camera_pending_data, 'camera_active_count': camera_active_count,
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
        return render(request, "profile_technician.html", {'user': user_data})
    return render(request, "login.html")


def camera_data_show(request):
    if request.session.has_key('id'):
        camera_data = Camera_Name.objects.all().select_related("circle")
        return render(request, "show_camera_info_technician.html", {'camera': camera_data})
    return render(request, 'login.html')


def update_user_profile_show(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        return render(request, 'update_user_profile_technician.html', {'user': user_data})
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
                return redirect("/technician/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_technician.html', {'user': user_data})
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
                return redirect("/technician/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_technician.html', {'user': user_data})
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
        return redirect("/technician/index")

    return render(request, 'login.html')


def accept_camera(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status=1
        camera.save()
        return HttpResponseRedirect('/technician/index')
    return render(request, 'login.html')


def change_camera_status(request, id):
    if request.session.has_key('id'):
        camera = Camera_Name.objects.get(camera_id=id)
        camera.camera_status = 0
        camera.save()
        return HttpResponseRedirect('/technician/camera_info_show')
    return render(request, 'login.html')


