from django.urls import path
from . import views
app_name = 'cal'
urlpatterns = [


    path("event/", views.CalendarView.as_view(), name="event"),
    path('new/', views.event, name='event_new'),
    path('edit/<event_id>', views.event, name='event_edit'),

]

