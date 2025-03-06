from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import get_object_or_404, redirect
# Define the todo_list view function
def todo_list(request):
    todos = Todo.objects.order_by('-id')
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




def complete_todo(request, todo_id):
    print(f"Completing todo with ID: {todo_id}")
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')  # Redirect to the todo list page

def delete_todo(request, todo_id):
    print(f"Deleting todo with ID: {todo_id}")
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')