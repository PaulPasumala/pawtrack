from django.contrib import admin
from django.urls import path
from pets import views

urlpatterns = [
    
    path('', views.login_view, name='home_login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.create_account_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api_update_profile/', views.api_update_profile, name='api_update_profile'),
    path('book_vet_appointment/', views.book_vet_appointment, name='book_vet_appointment'),
    
    path('api_login/', views.api_login, name='api_login'),
    path('api_register/', views.api_register, name='api_register'),
    path('logout/', views.logout_user, name='logout'),
    path('cancel_vet_appointment/', views.cancel_vet_appointment, name='cancel_vet_appointment'),
    path('get_match_candidates/', views.get_match_candidates, name='get_match_candidates'),
    path('record_swipe/', views.record_swipe, name='record_swipe'),
    path('get_chat_inbox/', views.get_chat_inbox, name='get_chat_inbox'),
    path('get_chat_messages/', views.get_chat_messages, name='get_chat_messages'),
    path('send_chat_message/', views.send_chat_message, name='send_chat_message'),
    path('get_active_matches/', views.get_active_matches, name='get_active_matches'),
    path('update_match_status/', views.update_match_status, name='update_match_status'),

    path('admin/', admin.site.urls),
    path('submit_adoption/', views.submit_adoption, name='submit_adoption'),
    path('cancel_application/', views.cancel_application, name='cancel_application'),
    path('register_pet/', views.register_pet, name='register_pet'), 
    path('move_to_bin/', views.move_to_bin, name='move_to_bin'),
    path('restore_pet/', views.restore_pet, name='restore_pet'),
    path('empty_bin/', views.empty_bin, name='empty_bin'),
]