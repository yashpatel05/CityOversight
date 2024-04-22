from django.db import models

# Create your models here.


class Camera_State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=40)

    class Meta:
        db_table = "camera_state"


class Camera_City(models.Model):
    city_id = models.AutoField(primary_key=True)
    state = models.ForeignKey(Camera_State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=40)

    class Meta:
        db_table = "camera_city"


class Camera_Circle(models.Model):
    circle_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(Camera_City, on_delete=models.CASCADE)
    circle_name = models.CharField(max_length=40)

    class Meta:
        db_table = "camera_circle"


class Camera_Name(models.Model):
    camera_id = models.AutoField(primary_key=True)
    circle = models.ForeignKey(Camera_Circle, on_delete=models.CASCADE)
    camera_name = models.CharField(max_length=40)
    camera_ip_addr = models.CharField(max_length=30, unique=True, default='0.0.0.0')
    camera_status = models.IntegerField(max_length=1, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "camera_name"


class User_Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=40)

    class Meta:
        db_table = "user_role"


class User_Signup(models.Model):
    user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(User_Role, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=70, unique=True)
    aadhar_card = models.CharField(max_length=14, unique=True)
    contact_no = models.BigIntegerField(max_length=15, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user_status = models.IntegerField(max_length=1, default=0)
    complain_points = models.IntegerField(max_length=3, default=100)
    profile_photo = models.CharField(max_length=500, default='blank_user.png')
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(max_length=1, null=True)
    otp_email = models.CharField(max_length=10, null=True)
    is_valid = models.IntegerField(max_length=1, null=True)

    class Meta:
        db_table = "user_signup"


class Report_Details(models.Model):
    report_id = models.AutoField(primary_key=True)
    camera = models.ForeignKey(Camera_Name, on_delete=models.CASCADE)
    generated_date = models.DateTimeField(auto_now_add=True)
    garbage_detection = models.IntegerField(max_length=1, default=0)
    pothole_detection = models.IntegerField(max_length=1, default=0)
    hand_gesture_detection = models.IntegerField(max_length=1, default=0)
    captured_image = models.CharField(max_length=500, default='white-background.jpg')
    scanned_image = models.CharField(max_length=500, default='white-background.jpg')
    report_status = models.IntegerField(max_length=1, default=0)

    class Meta:
        db_table = "report_details"


class User_Complain(models.Model):
    complain_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User_Signup, on_delete=models.CASCADE)
    uploaded_image = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    solved_date = models.DateTimeField(null=True)
    complain_status = models.IntegerField(max_length=1, default=0)
    deduction_points = models.IntegerField(max_length=3, default=0)
    city = models.ForeignKey(Camera_City, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_complain"
