from django.shortcuts import render, redirect
from .models import Todo
# Define the todo_list view function
def todo_list(request):
    # Ensure this line is indented properly
    return render(request, 'todo/index.html')

    def create_todo(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            Todo.objects.create(title=title, description=description)

            return redirect('todo_list')
            return render(request, 'todo/create_todo.html')