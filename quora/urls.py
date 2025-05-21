
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('notifications/', views.notification_view, name='notifications'),
     path('contactus/', views.contactus, name='contactus'),
    
]
