from django import forms

from CityWebsite.models import User_Role,Camera_State,Camera_City,Camera_Circle,Camera_Name,User_Signup,User_Complain,Report_Details
from parsley.decorators import parsleyfy


@parsleyfy
class UserRoleForm(forms.ModelForm):
    class Meta:
        model = User_Role
        fields = ["role_name"]


@parsleyfy
class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User_Signup
        fields = ["first_name","last_name","email","password","contact_no","aadhar_card","role"]


@parsleyfy
class EditUserSignupForm(forms.ModelForm):
    class Meta:
        model = User_Signup
        fields = ["first_name","last_name","email","contact_no"]


@parsleyfy
class EditUserProfileForm(forms.ModelForm):
    profile_photo = forms.FileField()
    class Meta:
        model = User_Signup
        fields = ["profile_photo"]


@parsleyfy
class CameraStateForm(forms.ModelForm):
    class Meta:
        model = Camera_State
        fields = ["state_name"]


@parsleyfy
class CameraCityForm(forms.ModelForm):
    class Meta:
        model = Camera_City
        fields = ["city_name","state"]


@parsleyfy
class CameraCircleForm(forms.ModelForm):
    class Meta:
        model = Camera_Circle
        fields = ["circle_name","city"]


@parsleyfy
class CameraInfoForm(forms.ModelForm):
    class Meta:
        model = Camera_Name
        fields = ["camera_name","camera_ip_addr","circle"]


@parsleyfy
class NewComplainForm(forms.ModelForm):
    uploaded_image = forms.FileField()
    class Meta:
        model = User_Complain
        fields = ["address","city","uploaded_image","description","user"]


@parsleyfy
class NewReportForm(forms.ModelForm):
    captured_image = forms.FileField()
    class Meta:
        model = Report_Details
        fields = ["captured_image"]
