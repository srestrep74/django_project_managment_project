from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

def index(request):
    projects = Project.objects.all()

    view_data = {
        'projects' : projects
    }

    return render(request, 'index_project.html', {'view_data' : view_data})

def show(request, project_id):
    project = Project.objects.get(id=project_id)

    view_data = {
        'project' : project,
    }

    return render(request, 'show_project.html', {'view_data' : view_data})

def create(request):
    return render(request, 'create_project.html')

def save(request) : 
    form = ProjectForm(request.POST)

    if form.is_valid() : 
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        try:
            project = Project()
            project.set_name(name)
            project.set_description(description)
            project.set_start_date(start_date)
            project.set_end_date(end_date)

            project.save()

            messages.success(request, "Project created successfully !")

            return redirect('index_project')
        except Exception as e:
            error_message = f'Error while saving the project : {str(e)}'
            form.add_error(None, error_message)
    else : 
        error_message = f'Error in the form '
        form.add_error(None, error_message)
    
    view_data = {
        'form' : form
    }

    return render(request, 'create_project.html',  {'view_data' : view_data})

def delete(request, project_id):
    project = Project.objects.get(id=project_id)

    view_data = {
        'project' : project,
    }

    return render(request, 'delete_project.html', {'view_data' : view_data})

def destroy(request, project_id):
    try : 
        project = Project.objects.get(id=project_id)
        project.delete()

        messages.success(request, "Project deleted successfully !")
    except Project.DoesNotExist:
        messages.error(request, "Project not found.")
    except Exception as e:
        messages.error(request, f"Error deleting project: {str(e)}")
    
    return redirect('index_project')

def edit(request, project_id ):
    project = Project.objects.get(id=project_id)

    view_data = {
        'project' : project,
    }

    return render(request, 'edit_project.html', {'view_data' : view_data})

def update(request, project_id):
    form = ProjectForm(request.POST)

    if form.is_valid() :
        
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date'] 

        try:
            project = Project.objects.get(id=project_id)
            project.set_name(name)
            project.set_description(description)
            project.set_start_date(start_date)
            project.set_end_date(end_date)

            project.save()

            messages.success(request, "Project updated successfully !")

            return redirect('index_project')
        except Exception as e:
            error_message = f'Error while updating the project : {str(e)}'
            form.add_error(None, error_message)
    else : 
        error_message = f'Error in the form '
        form.add_error(None, error_message)
    
    view_data = {
        'form' : form
    }

    return render(request, 'edit_project.html',  {'view_data' : view_data})