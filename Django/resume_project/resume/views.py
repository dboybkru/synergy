from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm

def resume_view(request):
    resume = Resume.objects.first()
    return render(request, 'resume/resume.html', {'resume': resume})

def edit_resume(request):
    resume = Resume.objects.first()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'resume/edit_resume.html', {'form': form})