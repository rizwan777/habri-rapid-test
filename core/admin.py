from django.contrib import admin
from core.models import Student,Parent,AcedemicDetail,Documents,Profile


class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name','email','gender','mobile','aadhar_no','profile_picture','aadhar_picture','height','date_of_birth','address','locality','city','state','country')
    exclude = ('password1','password2')
    list_display =('id','first_name', 'last_name','email','profile_completed','created_at','updated_at')

class ParentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name','email','gender','aadhar_no','relationship_to_student','relationship_desc','profile_picture','aadhar_picture','profession','designation')
    exclude = ('password1','password2')
    list_display =('id','student_id', 'first_name','last_name','email','created_at','updated_at')


class AcedemicAdmin(admin.ModelAdmin):
    fields=("student_id","in_class_of","section")
    list_display=("id","student_id","enrollment_id","in_class_of","section", 'created_at','updated_at')


class DocumentAdmin(admin.ModelAdmin):
    list_display=("id","student_id","type_of_doc","doc",'created_at','updated_at')

class ProfileAdmin(admin.ModelAdmin):
    fields=("student_id","parent_id","acedemic_id")
    list_display=("id","student_id","parent_id","acedemic_id","document_id","email_to_std_sent","email_to_admin_sent",'created_at','updated_at')



admin.site.register(Student,StudentAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(AcedemicDetail,AcedemicAdmin)
admin.site.register(Documents,DocumentAdmin)
admin.site.register(Profile,ProfileAdmin)