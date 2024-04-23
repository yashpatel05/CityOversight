from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import  sys
from CityWebsite.functions import handle_uploaded_file_photo,handle_uploaded_file
from django.contrib import messages
from CityWebsite.models import User_Signup,User_Role,User_Complain,Camera_Circle,Camera_City,Camera_Name,Camera_State,Report_Details
from CityWebsite.forms import UserRoleForm, CameraStateForm, CameraCityForm, CameraCircleForm, CameraInfoForm, \
    UserSignupForm, NewComplainForm, EditUserSignupForm, EditUserProfileForm


# Create your views here.


def index(request):
    if request.session.has_key('id'):
        complain_data_pending = User_Complain.objects.filter(complain_status=1, user_id=request.session['id'])
        complain_data_solved = User_Complain.objects.filter(complain_status=3, user_id=request.session['id'])
        complain_data_rejected = User_Complain.objects.filter(complain_status=2, user_id=request.session['id'])

        complain_data_pending_count = User_Complain.objects.filter(complain_status=1, user_id=request.session['id']).count()
        complain_data_solved_count = User_Complain.objects.filter(complain_status=3, user_id=request.session['id']).count()
        complain_data_rejected_count = User_Complain.objects.filter(complain_status=2, user_id=request.session['id']).count()


        garbage_report_solved_count = Report_Details.objects.filter(report_status=3).count()
        complain_solved_count = User_Complain.objects.filter(complain_status=3).count()
        complain_pending_count = User_Complain.objects.filter(complain_status=1).count()
        report_pending_count = Report_Details.objects.filter(report_status=1).count()

        return render(request, "index_citizen.html", {'complain_pending': complain_data_pending, 'complain_solved': complain_data_solved,
                                                      'complain_rejected': complain_data_rejected, 'my_complain_pending_count': complain_data_pending_count,
                                                      'my_complain_solved_count': complain_data_solved_count, 'my_complain_rejected_count': complain_data_rejected_count,
                                                      'report_solved_count': garbage_report_solved_count, 'complain_solved_count': complain_solved_count,
                                                      'complain_pending_count': complain_pending_count, 'report_pending_count': report_pending_count,
                                                      'complain_data_solved': complain_data_solved})
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
        return render(request, "profile_citizen.html", {'user': user_data})
    return render(request, "login.html")


def garbage_report_pending_show(request):
    if request.session.has_key('id'):
        garbage_report_pending = Report_Details.objects.filter(report_status=1).select_related("camera")
        return render(request, "show_garbage_report_pending.html", {'garbage_pending': garbage_report_pending})
    return render(request, 'login.html')


def garbage_report_solved_show(request):
    if request.session.has_key('id'):
        garbage_report_solved = Report_Details.objects.filter(report_status=3).select_related("camera")
        return render(request, "show_garbage_report_solved.html", {'garbage_solved': garbage_report_solved})
    return render(request, 'login.html')


def complain_pending_show(request):
    if request.session.has_key('id'):
        complain_data_pending = User_Complain.objects.filter(complain_status=1).select_related("user")
        return render(request, "show_complain_data_pending.html", {'complain_pending': complain_data_pending})
    return render(request, 'login.html')


def complain_solved_show(request):
    if request.session.has_key('id'):
        complain_data_solved = User_Complain.objects.filter(complain_status=3).select_related("user")
        return render(request, "show_complain_data_solved.html", {'complain_solved': complain_data_solved})
    return render(request, 'login.html')


def insert_new_complain(request):
    state = Camera_State.objects.all()
    id = request.session['id']
    user_data = User_Signup.objects.get(user_id=id)
    complain_point = user_data.complain_points
    if request.session.has_key('id'):
        if complain_point > 0:
            if request.method=="POST":
                form = NewComplainForm(request.POST, request.FILES)
                print("----------", form.errors)
                if form.is_valid():
                    try:
                        handle_uploaded_file(request.FILES['uploaded_image'])
                        form.save()
                        return redirect('/citizen/index')
                    except:
                        pass
                        print("------ Error -----",sys.exc_info())
            else:
                form = NewComplainForm()
                return render(request, 'insert_new_complain_citizen.html', {'form': form, 'state': state,'point': complain_point})
        else:
            messages.error(request, "You can't complain as Your complain point is 0 !!!")
            return render(request, "insert_new_complain_citizen.html", {'point': complain_point})
    return render(request, 'login.html')


def update_user_profile_show(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_data = User_Signup.objects.get(user_id=id)
        return render(request, 'update_user_profile_citizen.html', {'user': user_data})
    return render(request, "login.html")


def update_my_complain_show(request, id):
    state = Camera_State.objects.all()
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        return render(request, 'update_my_complain_citizen.html', {'complain': complain, 'state':state})
    return render(request, "login.html")


def my_complain_show(request):
    if request.session.has_key('id'):
        id = request.session['id']
        user_complain = User_Complain.objects.filter(user_id=id, complain_status=0)
        return render(request, 'my_complain_show_citizen.html', {'complain': user_complain})
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
                return redirect("/citizen/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_citizen.html', {'user': user_data})
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

                return redirect("/citizen/index")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_user_profile_citizen.html', {'user': user_data})
    return render(request, 'login.html')


def edit_my_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        form =  NewComplainForm(request.POST, request.FILES, instance=complain)
        print("------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['uploaded_image'])
                form.save()
                return redirect("/citizen/my_complain_show")
            except:
                pass
                print("------ Error -----", sys.exc_info())

        return render(request, 'update_my_complain_citizen.html', {'complain': complain})
    return render(request, 'login.html')


def delete_my_complain(request, id):
    if request.session.has_key('id'):
        complain = User_Complain.objects.get(complain_id=id)
        complain.delete()
        return redirect("/citizen/my_complain_show")
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

        return redirect("/citizen/index")

    return render(request, 'login.html')


def load_city(request):
    if request.session.has_key('id'):
        sid = request.GET.get('state')
        city = Camera_City.objects.filter(state_id=sid)
        return render(request, 'load_city_citizen.html', {'city': city})
    return render(request, 'login.html')