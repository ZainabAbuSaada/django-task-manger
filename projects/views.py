from django.shortcuts import render
from .models import Project, Task

def dashboard(request):
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='done').count()
    in_progress_tasks = Task.objects.filter(status='in_progress').count()

    context = {
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
    }

    return render(request, 'projects/dashboard.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {
        'projects': projects
    })

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'projects/portfolio.html', {
        'projects': projects
    })


