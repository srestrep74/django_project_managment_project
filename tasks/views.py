from django.shortcuts import render, redirect
from django.contrib import messages
from projects.models import Project
from .models import Task
from .forms  import TaskForm

# Create your views here.

def get_tasks(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = project.get_tasks()

    view_data = {
        'project' : project,
        'tasks' : tasks,
    }

    return render(request, 'project_tasks.html', {'view_data' : view_data})


def create(request, project_id):

    project = Project.objects.get(id=project_id)

    view_data = { 
        'project' : project,
    }

    return render(request, 'create_task.html', {'view_data' : view_data})

def save(request, project_id):
    form = TaskForm(request.POST)

    if form.is_valid() : 
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        status = form.cleaned_data['status']

        try:

            task = Task()

            task.set_name(name)
            task.set_descriptoin(description)
            task.set_status(status)
            task.set_project(Project.objects.get(id=project_id))

            task.save()

            messages.success(request, "Task created successfully !")

            return redirect('get_tasks', project_id=project_id)
        except Exception as e:
            error_message = f'Error while saving the task : {str(e)}'
            form.add_error(None, error_message)
    else : 
        error_message = f'Error in the form '
        form.add_error(None, error_message)
    
    view_data = {
        'form' : form
    }

    return render(request, 'create_task.html',  {'view_data' : view_data})

def edit(request, task_id):
    task = Task.objects.get(id=task_id)

    view_data = {
        'task' : task,
    }

    return render(request, 'edit_task.html', {'view_data' : view_data})

def update(request, task_id):
    form = TaskForm(request.POST)

    if form.is_valid() : 
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        status = form.cleaned_data['status']

        try:
            task = Task.objects.get(id=task_id)
            task.set_name(name)
            task.set_descriptoin(description)
            task.set_status(status)    
    
            task.save()

            messages.success(request, "Task updated successfully !")

            return redirect('get_tasks', project_id=task.get_project().id)
        except Exception as e:
            error_message = f'Error while updating the task : {str(e)}'
            form.add_error(None, error_message)
    else : 
        error_message = f'Error in the form '
        form.add_error(None, error_message)
    
    view_data = {
        'form' : form
    }

    return render(request, 'edit_task.html',  {'view_data' : view_data})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    view_data = {
        'task' : task,
    }

    return render(request, 'delete_task.html', {'view_data' : view_data})

def destroy(request, task_id):
    task = Task.objects.get(id=task_id)
    try : 
        task.delete()

        messages.success(request, "Task deleted successfully !")
    except Project.DoesNotExist:
        messages.error(request, "Taks not found.")
    except Exception as e:
        messages.error(request, f"Error deleting task: {str(e)}")
    
    return redirect('get_tasks', project_id=task.get_project().get_id())

def dones(request):
    tasks = Task.get_completed_tasks()

    view_data = {
        'section' : 'Completed Tasks',
        'tasks' : tasks,
    }

    return render(request, "index_tasks.html", {'view_data' : view_data})

def in_progress(request):
    tasks = Task.get_in_progress_tasks()

    view_data = {
        'section' : 'In Progress Tasks',
        'tasks' : tasks,
    }

    return render(request, "index_tasks.html", {'view_data' : view_data})

def undone(request):
    tasks = Task.get_not_started_tasks()

    view_data = {
        'section' : 'Not Started Tasks',
        'tasks' : tasks,
    }

    return render(request, "index_tasks.html", {'view_data' : view_data})