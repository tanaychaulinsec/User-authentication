from django.contrib import admin
from django.urls import path
from usersAccount import views

app_name = 'usersAccount'

urlpatterns = [
    path('/',views.index,name='index'),
    path('admin/', admin.site.urls),
]