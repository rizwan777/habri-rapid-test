from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from .constant import *
import uuid
import random
from datetime import datetime
# Create your models here.

def generate_enrollment_id(student_id):
    try:
        # Get the student first
        student_name = Student.objects.get(email=student_id).first_name

        # Get the current date in DDMMYY format
        current_date = datetime.now().strftime('%d%m%y')
        # Make sure student name is at least 3 characters long
        if len(student_name) < 3:
            student_name = student_name + 'X' * (3 - len(student_name))
        # Get the first three letters of the student name
        name_prefix = student_name[:3].upper()

        # Generate a random 3-digit number between 1 and 999
        random_suffix = str(random.randint(1, 999)).zfill(3)

        # Combine the parts to create the enrollment ID
        enrollment_id = current_date + name_prefix + random_suffix

        return enrollment_id
    except Student.DoesNotExist():
        return False

class BaseModel(models.Model):
    remarks = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Student(AbstractBaseUser,BaseModel):
    first_name = models.CharField(max_length=128, blank=True, null=True, default='')
    last_name = models.CharField(max_length=128, blank=True, null=True, default='')
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100, blank=True)
    aadhar_no = models.IntegerField(blank=False,null=False, unique=True)
    profile_picture = models.ImageField(upload_to='student_profile/', blank=True, null=True)
    aadhar_picture = models.ImageField(upload_to='student_aadhar/', blank=True, null=True)
    mobile = models.CharField(max_length=128, blank=True, null=True)
    height = models.CharField(max_length=120,blank=True,null=True)
    date_of_birth = models.DateField(editable=True, null=True,blank=True)
    state = models.CharField(max_length=1024, blank=True, null=True)
    city = models.CharField(max_length=1024, blank=True, null=True)
    country = models.CharField(max_length=1024, blank=True, null=True)
    locality = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    profile_completed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # class Meta:
    #     fields =['first_name','email']

class Parent(AbstractBaseUser,BaseModel):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True, default='')
    last_name = models.CharField(max_length=128, blank=True, null=True, default='')
    email = models.EmailField(max_length=255, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100, blank=True)
    relationship_to_student = models.CharField(choices=ROLES_CHOICES, max_length=100, blank=True)
    relationship_desc = models.CharField(max_length=50,null=True, blank=True)
    aadhar_no = models.IntegerField(blank=False,null=False,unique=True)
    profile_picture = models.ImageField(upload_to='parents_profile/', blank=True, null=True)
    aadhar_picture = models.ImageField(upload_to='parents_aadhar/', blank=True, null=True)
    profession = models.CharField(max_length=50,null=True, blank=True)
    designation = models.CharField(max_length=50,null=True, blank=True)

    USERNAME_FIELD = 'email'

class AcedemicDetail(BaseModel):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    enrollment_id = models.CharField(max_length=50,blank=True,null=True)
    in_class_of = models.IntegerField(null=False,blank=False)
    section = models.CharField(max_length=20,blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.enrollment_id :
            try:
                # call the helper method to set value for enrollment
                valueGot = generate_enrollment_id(self.student_id)
                if valueGot is not False:
                    # add generated value for enrollment_id
                    self.enrollment_id = valueGot
                    super(AcedemicDetail,self).save(*args,**kwargs)
                else:
                    # student is not present
                    return False
            except Exception as e:
                # some issue encounter
                return str(e)

class Documents(BaseModel):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    type_of_doc = models.CharField(choices=DOCUMENT_CHOICES, max_length=100, blank=True)
    doc = models.ImageField(upload_to='documents/', blank=True, null=True)
    doc_desc = models.CharField(max_length=50,null=True, blank=True)



class Profile(BaseModel):
    student_id = models.OneToOneField(Student,on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent,on_delete=models.PROTECT,null=True,blank=True)
    acedemic_id = models.ForeignKey(AcedemicDetail,on_delete=models.PROTECT,null=True,blank=True)
    document_id = models.BooleanField(default=False)
    email_to_std_sent = models.BooleanField(default=False)
    email_to_admin_sent = models.BooleanField(default=False)









