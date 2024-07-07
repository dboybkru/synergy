# resume/admin.py
from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основная информация', {'fields': ['photo', 'about_me', 'desired_position', 'contacts']}),
        ('Образование и опыт', {'fields': ['education', 'education_files', 'work_experience', 'additional_info']}),
    ]
    list_display = ('desired_position', 'contacts')

admin.site.register(Resume, ResumeAdmin)
admin.site.site_header = "Администрирование резюме"
admin.site.site_title = "Админка резюме"
admin.site.index_title = "Добро пожаловать в админку резюме"
