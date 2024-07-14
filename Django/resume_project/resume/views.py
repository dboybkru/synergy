# # resume/views.py
# from django.shortcuts import render, redirect
# from .models import Resume, EducationFile, Certificate
# from .forms import ResumeForm, EducationFileForm

# def resume_view(request):
#     resume = Resume.objects.first()
#     return render(request, 'resume/resume.html', {'resume': resume})

# def edit_resume(request):
#     resume = Resume.objects.first()
#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES, instance=resume)
#         if form.is_valid():
#             resume = form.save()
#             for file in request.FILES.getlist('education_files'):
#                 education_file = EducationFile(file=file)
#                 education_file.save()
#                 resume.education_files.add(education_file)
#             resume.save()
#             return redirect('resume')
#     else:
#         form = ResumeForm(instance=resume)
#     return render(request, 'resume/edit_resume.html', {'form': form})

# resume/views.py
from django.shortcuts import render
from .models import Resume

def resume_view(request):
    resume = Resume.objects.first()  # Или используйте другой способ получения резюме
    return render(request, 'resume/resume.html', {'resume': resume})

def edit_resume(request):
    # Логика для редактирования резюме
    pass
