from django.contrib import admin
from django.urls import path, include
from Admins import admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', admin_views.index),
    path('logout1/', admin_views.logout),
    path('profile/', admin_views.profile),

    path('user_signup/', admin_views.user_signup_show),
    path('user_role/', admin_views.user_role_show),
    path('state/', admin_views.camera_state_show),
    path('city/', admin_views.camera_city_show),
    path('circle/', admin_views.camera_circle_show),
    path('camera/', admin_views.camera_data_show),
    path('report/', admin_views.garbage_report_show),
    path('complain/', admin_views.complain_data_show),

    path('delete_state/<int:id>', admin_views.camera_state_delete),
    path('delete_city/<int:id>', admin_views.camera_city_delete),
    path('delete_circle/<int:id>', admin_views.camera_circle_delete),
    path('delete_camera/<int:id>', admin_views.camera_delete),

    path('insert_camera_state/', admin_views.insert_camera_state),
    path('insert_camera_city/', admin_views.insert_camera_city),
    path('insert_camera_circle/', admin_views.insert_camera_circle),
    path('insert_camera_info/', admin_views.insert_camera_info),

    path('update_camera_state_show/<int:id>', admin_views.update_camera_state_show),
    path('update_camera_city_show/<int:id>', admin_views.update_camera_city_show),
    path('update_camera_circle_show/<int:id>', admin_views.update_camera_circle_show),
    path('update_camera_info_show/<int:id>', admin_views.update_camera_info_show),
    path('update_user_profile_show/', admin_views.update_user_profile_show),

    path('edit_camera_state/<int:id>', admin_views.edit_camera_state),
    path('edit_camera_city/<int:id>', admin_views.edit_camera_city),
    path('edit_camera_circle/<int:id>', admin_views.edit_camera_circle),
    path('edit_camera_info/<int:id>', admin_views.edit_camera_info),
    path('edit_user_profile/', admin_views.edit_user_profile),
    path('edit_user_profile_photo/', admin_views.edit_user_profile_photo),

    path('remove_user_profile_photo/', admin_views.remove_user_profile_photo),

    path('accept_user/<int:id>', admin_views.accept_user_signup),
    path('accept_camera/<int:id>', admin_views.accept_camera),
    path('accept_garbage_report/<int:id>', admin_views.accept_garbage_report),
    path('accept_complain/<int:id>', admin_views.accept_complain),

    path('reject_user/<int:id>', admin_views.reject_user_signup),
    path('reject_camera/<int:id>', admin_views.reject_camera),
    path('reject_garbage_report/<int:id>', admin_views.reject_garbage_report),
    path('reject_complain/<int:id>', admin_views.reject_complain),

    path('solved_complain/<int:id>', admin_views.solved_complain),
    path('solved_garbage/<int:id>', admin_views.solved_garbage),

    path('change_user_status/<int:id>', admin_views.change_user_status),
    path('change_camera_status/<int:id>', admin_views.change_camera_status),

    path('ajax/load-cities/', admin_views.load_city, name='ajax_load_city'),
    path('ajax/load-circle/', admin_views.load_circle, name='ajax_load_circle'),

]


