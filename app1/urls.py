from django.urls import path
from .views import edit, hello,signup,show,delete,edit,update,login,logout

urlpatterns = [
    path('hello/',hello),
    path('signup/',signup),
    path('show/',show,name='show'),
    path('delete/<int:id>/',delete),
    path('edit/<int:id>/',edit),
    path('update/<int:id>/',update),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout')
]