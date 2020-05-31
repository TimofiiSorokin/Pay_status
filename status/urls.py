from django.urls import path

from status import views
app_name = 'status'

urlpatterns = [
    path('', views.home_page, name='status_page'),
    path('ajax_add/', views.ajax_add, name='ajax_add'),
    path('ajax_edit/', views.ajax_edit, name='ajax_edit'),
    path('ajax_delete/', views.ajax_delete, name='ajax_delete'),
]