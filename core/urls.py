from django.contrib import admin
from django.urls import path, include
from home import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.home, name='home'),  # Home page
    path('tasks/', include('task.urls')),    # Task routes
    path('accounts/', include('accounts.urls')),  # ✅ custom auth
]
