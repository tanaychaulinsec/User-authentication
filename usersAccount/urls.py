from django.urls import path, include
from usersAccount import views

# SET THE NAMESPACE!
app_name = 'usersAccount'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/',views.user_login,name='login'),
]