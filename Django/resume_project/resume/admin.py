# # resume/admin.py
# from django.contrib import admin
# from .models import Resume, Certificate

# class CertificateAdmin(admin.ModelAdmin):
#     list_display = ('file',)

# class ResumeAdmin(admin.ModelAdmin):
#     list_display = ('desired_position', 'phone_number', 'contacts')
#     filter_horizontal = ('education_files',)
#     fieldsets = [
#         ('Основная информация', {'fields': ['photo', 'about_me', 'desired_position', 'contacts', 'phone_number']}),
#         ('Образование и опыт', {'fields': ['education', 'education_files', 'work_experience', 'additional_info']}),
#     ]

# admin.site.register(Resume, ResumeAdmin)
# admin.site.register(Certificate, CertificateAdmin)
# admin.site.site_header = "Администрирование резюме"
# admin.site.site_title = "Админка резюме"
# admin.site.index_title = "Добро пожаловать в админку резюме"

# resume/admin.py
from django.contrib import admin
from .models import Resume, Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('file',)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('desired_position', 'phone_number', 'contacts')
    filter_horizontal = ('education_files',)
    fieldsets = [
        ('Основная информация', {'fields': ['photo', 'about_me', 'desired_position', 'contacts', 'phone_number']}),
        ('Образование и опыт', {'fields': ['education', 'education_files', 'work_experience', 'additional_info']}),
    ]

admin.site.register(Resume, ResumeAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.site_header = "Администрирование резюме"
admin.site.site_title = "Админка резюме"
admin.site.index_title = "Добро пожаловать в админку резюме"
