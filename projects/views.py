from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

def index(request):
    projects = Project.objects.all()

    view_data = {
        'projects' : projects
    }

    return render(request, 'index.html', {'view_data' : view_data})

def show(request, id):
    project = Project.objects.get(id=id)

    view_data = {
        'project' : project,
    }

    return render(request, 'show.html', {'view_data' : view_data})

def create(request):
    return render(request, 'create.html')

def save(request) : 
    form = ProjectForm(request.POST)

    if form.is_valid() : 
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        try:
            project = Project.objects.create(
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
            )

            messages.success(request, "Project created successfully !")

            return redirect('index')
        except Exception as e:
            error_message = f'Error while saving the project : {str(e)}'
            form.add_error(None, error_message)
    else : 
        error_message = f'Error in the form '
        form.add_error(None, error_message)
    
    view_data = {
        'form' : form
    }

    return render(request, 'create.html',  {'view_data' : view_data})

def delete(request, id):
    project = Project.objects.get(id=id)

    view_data = {
        'project' : project,
    }

    return render(request, 'delete.html', {'view_data' : view_data})

def destroy(request, id):
    try : 
        project = Project.objects.get(id=id)
        project.delete()

        messages.success(request, "Project deleted successfully !")
    except Project.DoesNotExist:
        messages.error(request, "Project not found.")
    except Exception as e:
        messages.error(request, f"Error deleting project: {str(e)}")
    
    return redirect('index')

def edit(request, id ):
    project = Project.objects.get(id=id)

    view_data = {
        'project' : project,
    }

    return render(request, 'edit.html', {'view_data' : view_data})

def update(request, id):
    form = ProjectForm(request.POST)

    if form.is_valid() : 
        try:
            project = Project.objects.get(id=id)
            project.name = request.POST.get('name')
            project.description = request.POST.get('description')
            project.start_date = request.POST.get('start_date')
            project.end_date = request.POST.get('end_date')

            project.save()

            messages.success(request, "Project updated successfully !")

            return redirect('index')
        except Exception as e:
            error_message = f'Error while updating the project : {str(e)}'
            form.add_error(None, error_message)
    else : 
        error_message = f'Error in the form '
        form.add_error(None, error_message)
    
    view_data = {
        'form' : form
    }

    return render(request, 'edit.html',  {'view_data' : view_data})