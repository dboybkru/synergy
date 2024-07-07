# resume/forms.py
from django import forms
from .models import Resume, EducationFile

class EducationFileForm(forms.ModelForm):
    class Meta:
        model = EducationFile
        fields = ['file']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'photo': 'Фото',
            'about_me': 'О себе',
            'education': 'Образование',
            'education_files': 'Аттестаты (PDF)',
            'work_experience': 'Опыт работы',
            'desired_position': 'Желаемая должность',
            'additional_info': 'Дополнительная информация',
            'contacts': 'Контакты',
        }
        widgets = {
            'education_files': forms.CheckboxSelectMultiple,
        }
