"""CityOversight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CityWebsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('forgot/', views.forgot),
    path('send_email/', views.sendemail),
    path('reset_password/', views.set_password),
    path('profile/', views.profile),
    path('email_verification/', views.email_verification),

    path('user_signup/', views.user_signup_show),
    path('user_role/', views.user_role_show),
    path('state/', views.camera_state_show),
    path('city/', views.camera_city_show),
    path('circle/', views.camera_circle_show),
    path('camera/', views.camera_data_show),
    path('report/', views.garbage_report_show),
    path('complain/', views.complain_data_show),

    path('delete_state/<int:id>', views.camera_state_delete),
    path('delete_city/<int:id>', views.camera_city_delete),
    path('delete_circle/<int:id>', views.camera_circle_delete),
    path('delete_camera/<int:id>', views.camera_delete),
    path('delete_user_role/<int:id>', views.user_role_delete),

    path('insert_user_role/', views.insert_user_role),
    path('insert_camera_state/', views.insert_camera_state),
    path('insert_camera_city/', views.insert_camera_city),
    path('insert_camera_circle/', views.insert_camera_circle),
    path('insert_camera_info/', views.insert_camera_info),

    path('update_user_role_show/<int:id>', views.update_user_role_show),
    path('update_camera_state_show/<int:id>', views.update_camera_state_show),
    path('update_camera_city_show/<int:id>', views.update_camera_city_show),
    path('update_camera_circle_show/<int:id>', views.update_camera_circle_show),
    path('update_camera_info_show/<int:id>', views.update_camera_info_show),
    path('update_user_profile_show/', views.update_user_profile_show),

    path('edit_user_role/<int:id>', views.edit_user_role),
    path('edit_camera_state/<int:id>', views.edit_camera_state),
    path('edit_camera_city/<int:id>', views.edit_camera_city),
    path('edit_camera_circle/<int:id>', views.edit_camera_circle),
    path('edit_camera_info/<int:id>', views.edit_camera_info),
    path('edit_user_profile/', views.edit_user_profile),
    path('edit_user_profile_photo/', views.edit_user_profile_photo),

    path('remove_user_profile_photo/', views.remove_user_profile_photo),

    path('accept_user/<int:id>', views.accept_user_signup),
    path('accept_camera/<int:id>', views.accept_camera),
    path('accept_garbage_report/<int:id>', views.accept_garbage_report),
    path('accept_complain/<int:id>', views.accept_complain),

    path('reject_user/<int:id>', views.reject_user_signup),
    path('reject_camera/<int:id>', views.reject_camera),
    path('reject_garbage_report/<int:id>', views.reject_garbage_report),
    path('reject_complain/<int:id>', views.reject_complain),

    path('solved_complain/<int:id>', views.solved_complain),
    path('solved_garbage/<int:id>', views.solved_garbage),

    path('change_user_status/<int:id>', views.change_user_status),
    path('change_camera_status/<int:id>', views.change_camera_status),

    path('ajax/load-cities/', views.load_city, name='ajax_load_city'),
    path('ajax/load-circle/', views.load_circle, name='ajax_load_circle'),

    path('citizen/', include('Citizen.urls')),
    path('technician/', include('Technician.urls')),
    path('admin/', include('Admins.urls')),
    path('employee/', include('Employee.urls')),

]


