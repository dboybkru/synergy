# # resume/models.py
# from django.db import models

# class Certificate(models.Model):
#     file = models.FileField(upload_to='education_files/')

#     def __str__(self):
#         return self.file.name

# class EducationFile(models.Model):
#     file = models.FileField(upload_to='education_files/', verbose_name='Файл аттестата')

#     def __str__(self):
#         return self.file.name

#     class Meta:
#         verbose_name = 'Файл аттестата'
#         verbose_name_plural = 'Файлы аттестатов'

# class Resume(models.Model):
#     photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
#     about_me = models.TextField(verbose_name='О себе')
#     education = models.TextField(verbose_name='Образование')
#     education_files = models.ManyToManyField(EducationFile, blank=True, verbose_name='Аттестаты (PDF)')
#     work_experience = models.TextField(verbose_name='Опыт работы')
#     desired_position = models.CharField(max_length=100, verbose_name='Желаемая должность')
#     additional_info = models.TextField(verbose_name='Дополнительная информация')
#     contacts = models.TextField(verbose_name='Контакты')
#     phone_number = models.CharField(max_length=20, blank=True)  # Добавляем поле для номера телефона
#     education_files = models.ManyToManyField(Certificate, blank=True)  # Используем ManyToManyField для аттестатов

#     def __str__(self):
#         return self.desired_position

#     class Meta:
#         verbose_name = 'Резюме'
#         verbose_name_plural = 'Резюме'


# # resume/models.py
# # from django.db import models

# # class Certificate(models.Model):
# #     file = models.FileField(upload_to='certificates/')

# #     def __str__(self):
# #         return self.file.name

# # class Resume(models.Model):
# #     photo = models.ImageField(upload_to='photos/', blank=True, null=True)
# #     additional_info = models.TextField(blank=True)
# #     desired_position = models.CharField(max_length=255, blank=True)
# #     education = models.TextField(blank=True)
# #     work_experience = models.TextField(blank=True)
# #     about_me = models.TextField(blank=True)
# #     contacts = models.TextField(blank=True)
# #     phone_number = models.CharField(max_length=20, blank=True)
# #     education_files = models.ManyToManyField(Certificate, blank=True)

# #     def __str__(self):
# #         return self.desired_position


# resume/models.py
from django.db import models

class Certificate(models.Model):
    file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.file.name

class Resume(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    additional_info = models.TextField(blank=True)
    desired_position = models.CharField(max_length=255, blank=True)
    education = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    contacts = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    education_files = models.ManyToManyField(Certificate, blank=True)

    def __str__(self):
        return self.desired_position
