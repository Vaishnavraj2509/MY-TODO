from django.shortcuts import render, redirect
from .models import Todo
# Define the todo_list view function
def todo_list(request):
    todos = Todo.objects.all()
    # Ensure this line is indented properly
    return render(request, 'todo/index.html',{'todos':todos})



def create_todo(request):
    if request.method == 'POST':
        # Handle form submission
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
        return redirect('todo_list')  # Redirect to the todo list page
    return render(request, 'todo/create_todo.html')

    def complete_todo(request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.complete = True
        todo.save()
        return render('todo_list')

