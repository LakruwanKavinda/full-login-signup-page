from django.contrib import admin
from django.urls import path, include
from scanner.views import upload_pdf
from pages.views import home
from accounts.views import signup_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('upload-pdf/', upload_pdf, name='upload_pdf'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]
