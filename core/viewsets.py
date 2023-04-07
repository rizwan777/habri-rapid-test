from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import *
from core.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
# Create your views here.
import csv
import random,string




class CSVUploadView(APIView):
    def post(self, request):
        csv_file = request.FILES['file']
        # key = request.POST['student']
        # print("file==>",csv_file,key)
        if csv_file is not None:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            data = [row for row in reader]
            serializer = StudentSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'CSV data imported into database.'})
        else:
            return Response(serializer.errors, status=400)


class FinalUpdateOnProfile(APIView):

    def post(self, request):

        studentId = request.POST['student_id']
        studentObj = Student.objects.get(id=studentId)
        print("==>",studentObj)
        studentName = studentObj.first_name
        email = studentObj.email

        parentId = Parent.objects.filter(student_id=studentId).order_by('-created_at')[0].id
        enrollmentObj = AcedemicDetail.objects.filter(student_id=studentId).order_by('-created_at')[0]
        enrollment_id = enrollmentObj.enrollment_id
        courseID = enrollmentObj.in_class_of
        section_id = enrollmentObj.section

        # initializing size of string
        N = 7
        session_id = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))
        # docId = Documents.objects.filter(student_id=studentId).order_by('-created_at')[0].id

#       send to student
        # fname,enrolmentID
        std_res = send_email_to_student(studentName,email,enrollment_id)


        print("==>",studentName,courseID,section_id,enrollment_id,session_id)
        # send email to admin
        # stdName,clsName,sectionId,enrolmentId,sessionId
        adm_res = send_email_to_admin(studentName,courseID,section_id,enrollment_id,session_id)
        if adm_res:
            profilobj = Profile.objects.create(student_id= studentObj,document_id=True,email_to_admin_sent=True)
            profilobj.save()
        if std_res:
            profilobj = Profile.objects.create(student_id=studentObj,document_id=True,email_to_std_sent=True)
            profilobj.save()

        return Response({'status': 'Email has been sent to users'})



class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class ParentViewSet(ModelViewSet):
    serializer_class = ParentsSerializer
    queryset = Parent.objects.all()

class AcedemicDetailsViewSet(ModelViewSet):
    serializer_class = AcedemicDetailSerializer
    queryset = AcedemicDetail.objects.all()

class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()

    def create(self, request, *args, **kwargs):
        print("create callelled==>",self,request)
        # any method you want here
        return Response("response")
