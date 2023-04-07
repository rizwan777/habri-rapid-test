from rest_framework.routers import DefaultRouter
from core.viewsets import *
from django.urls import path

# creating Router object
router = DefaultRouter()


# Register view set with router
router.register('student', StudentViewSet, basename='Student_api')
router.register('parents', ParentViewSet, basename='parents_api')
router.register('docs', DocumentViewSet, basename='docs_api')
router.register('acedemic/details', AcedemicDetailsViewSet, basename='acedemic_detail_api')
router.register('profile/status', ProfileViewSet, basename='profile_api')



