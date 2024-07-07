from django.urls import path
from .views import resume_view, edit_resume

urlpatterns = [
    path('', resume_view, name='resume'),
    path('edit/', edit_resume, name='edit_resume'),
]
