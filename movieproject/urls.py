from django.contrib import admin
from django.urls import path
from movieapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path("addmovie/",views.addmovie,name="addmovie"),
    path("logout/",views.user_logout,name="logout"),
    path("profile/",views.profile,name="profile")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
