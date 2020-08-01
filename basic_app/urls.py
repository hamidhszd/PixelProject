from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Temlpate Tagging

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    
    path('photo_list/', views.PhotoListView.as_view(), name='photo_list'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),

    path("photo_delete/<int:pk>/",views.PhotoDeleteView.as_view(),name='photo_delete'),
    path("photo_upload/",views.PhotoUploadView,name='upload_photo'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



