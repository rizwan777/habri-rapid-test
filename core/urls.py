from django.urls import path, include, re_path
from core.viewsets import *

urlpatterns = [
    path('upload-csv', CSVUploadView.as_view(), name='csv-upload'),
    path('submit-application', FinalUpdateOnProfile.as_view(), name='csv-upload'),

]
