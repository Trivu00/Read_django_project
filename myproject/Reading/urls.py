from django.conf.urls import include
from django.urls import path

from Reading import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    
    path('about/', views.about_view, name='about'),
    path('read-page/<int:id>/', views.read_page_view, name='read-page'),
    path('reading/', views.reading_view, name='reading'),
    path('accounts',include('django.contrib.auth.urls')),
    
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registerPage,name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 