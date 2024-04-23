from django.contrib import admin
from django.urls import path
from Employee import employee_views

urlpatterns = [
    path('index/', employee_views.index),
    path('logout/', employee_views.logout),
    path('profile/', employee_views.profile),

    path('garbage_scan/', employee_views.camera_select_show),
    path('captured_image/', employee_views.captured_image),
    path('scanned_image/', employee_views.scanned_image),
    path('generate_report/', employee_views.generate_report),
    path('report/', employee_views.garbage_report_show),
    path('complain/', employee_views.complain_data_show),

    path('update_user_profile_show/', employee_views.update_user_profile_show),

    path('edit_user_profile/', employee_views.edit_user_profile),
    path('edit_user_profile_photo/', employee_views.edit_user_profile_photo),

    path('remove_user_profile_photo/', employee_views.remove_user_profile_photo),

    path('accept_user/<int:id>', employee_views.accept_user_signup),
    path('accept_camera/<int:id>', employee_views.accept_camera),
    path('accept_garbage_report/<int:id>', employee_views.accept_garbage_report),
    path('accept_complain/<int:id>', employee_views.accept_complain),

    path('reject_user/<int:id>', employee_views.reject_user_signup),
    path('reject_camera/<int:id>', employee_views.reject_camera),
    path('reject_garbage_report/<int:id>', employee_views.reject_garbage_report),
    path('reject_complain/<int:id>', employee_views.reject_complain),

    path('solved_complain/<int:id>', employee_views.solved_complain),
    path('solved_garbage/<int:id>', employee_views.solved_garbage),

    path('ajax/load-cities/', employee_views.load_city, name='ajax_load_city'),
    path('ajax/load-circle/', employee_views.load_circle, name='ajax_load_circle'),
    path('ajax/load-camera/', employee_views.load_camera, name='ajax_load_camera'),

    #path('garbage_report_pending/', employee_views.garbage_report_pending_show),
    #path('complain_pending/', employee_views.complain_pending_show),
    #path('garbage_report_solved/', employee_views.garbage_report_solved_show),
    #path('complain_solved/', employee_views.complain_solved_show),

]