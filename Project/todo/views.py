from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Show all tasks
def task_list(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("/")
    return render(request, "index.html", {"tasks": tasks})

# Add a task
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")

# Update a task (mark complete/incomplete)
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("task_list")
