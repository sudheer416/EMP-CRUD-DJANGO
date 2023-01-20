from django.urls import path
from . import views

urlpatterns = [
    # path('employee/', views.employee, name='employee'),
    # path('showemp/', views.showemployee),
    # path('reg/', views.registeremployee),

     path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]