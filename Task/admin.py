from django.contrib import admin
from .models import Task  # Ensure Task model is correctly imported

class TaskAdmin(admin.ModelAdmin):
    # Define your admin configurations here, e.g., fields to display
    list_display = ('title' ,'description', 'completed')  # Example fields

# Register the model and the admin class outside the class definition
admin.site.register(Task, TaskAdmin)
