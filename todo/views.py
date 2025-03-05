from django.shortcuts import render

# Define the todo_list view function
def todo_list(request):
    # Ensure this line is indented properly
    return render(request, 'todo/index.html')