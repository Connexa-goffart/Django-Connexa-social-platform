from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import analytics_dashboard, private_messages

app_name = 'users'

urlpatterns = [
    path('login/' , views.login_user , name = 'login'),
    path('logout/' ,views.logout_user , name = 'logout'),
    path('register/', views.register_user , name ='register'),
    path('profile/<str:pk>/' , views.profile_user , name ='profile'),
    path('user_edit/<str:pk>/' , views.edit_user , name ='edit_user'),
    path('' , views.welcome_user , name= "welcome"),
    path('search/', views.search_users, name='search_users'),
    path('follow/<str:pk>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:pk>/', views.unfollow_user, name='unfollow_user'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.create_group, name='create_group'),
    path('groups/<int:pk>/', views.group_profile_view, name='group_profile'),
    path('groups/<int:pk>/edit/', views.edit_group, name='edit_group'),
    path('groups/<int:pk>/join/', views.join_group, name='join_group'),
    path('groups/<int:pk>/leave/', views.leave_group, name='leave_group'),
    path('groups/<int:pk>/chat/', views.group_chat, name='group_chat'),
    path('groups/message/<int:msg_id>/edit/', views.edit_group_message, name='edit_group_message'),
    path('groups/message/<int:msg_id>/delete/', views.delete_group_message, name='delete_group_message'),
    path('groups/message/<int:msg_id>/react/<str:emoji>/', views.react_to_message, name='react_to_message'),
    path('groups/message/<int:msg_id>/pin/', views.pin_message, name='pin_message'),
    path('groups/message/<int:msg_id>/unpin/', views.unpin_message, name='unpin_message'),
    path('dashboard/', analytics_dashboard, name='analytics_dashboard'),
    path('messages/', private_messages, name='private_messages'),
    path('messages/<int:user_id>/', private_messages, name='private_messages'),
    path('settings/', views.user_settings, name='user_settings'),
    path('groups/<int:pk>/admin/', views.group_admin, name='group_admin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)