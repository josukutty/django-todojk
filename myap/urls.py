from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<str:details_id>',views.delete,name='delete')
]