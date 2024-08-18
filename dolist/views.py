from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib import messages

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method =="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        is_completed = request.POST.get('is_completed') == 'on'

        task = Task(title=title, description=description, due_date=due_date, is_completed=is_completed)
        task.save()
        messages.success(request, 'Task created successfully')

        return redirect('task_list')
    return render(request, 'task_form.html')
    
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('task_list')


# def delete_task(request, task_id):
#     task = Task.objects.filter(id=task_id)
#     task.delete()
#     return redirect('dolist/templates/task_list/')
   
# Create your views here.
