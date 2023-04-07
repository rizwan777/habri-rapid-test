from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import *


class StudentSerializer(ModelSerializer):
    '''
    Student Serializer
    '''

    class Meta:
        model = Student
        fields = ('id','first_name', 'last_name','email','gender','mobile','aadhar_no','height','date_of_birth','address','locality','city','state','country')

class ParentsSerializer(ModelSerializer):
    '''
    Parent Serializer
    '''

    class Meta:
        model = Parent
        fields = ('id','first_name', 'last_name','email','gender','aadhar_no','relationship_to_student','relationship_desc','profile_picture','aadhar_picture','profession','designation')

class DocumentsSerializer(ModelSerializer):
    '''
    Documents Serializer
    '''

    class Meta:
        model = Documents
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    '''
    Profile Serializer
    '''

    class Meta:
        model = Profile
        fields = '__all__'

class AcedemicDetailSerializer(ModelSerializer):
    '''
    AcedemicDetail Serializer
    '''

    class Meta:
        model = AcedemicDetail
        fields = '__all__'