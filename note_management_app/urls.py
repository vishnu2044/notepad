from django.urls import path
from . import views 


urlpatterns = [
    path('create_note/', views.create_note, name='create_note'),
    path('get_notes/', views.get_notes, name='get_notes'),
    path('get_single_note/<int:id>/', views.get_single_note, name='get_single_note'),
    path('update_note/<int:id>/', views.update_note, name='update_note'),
    path('delete_note/<int:id>/', views.delete_note, name='delete_note'),


]
    