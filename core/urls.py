from django.urls import path,reverse_lazy,include
from .views import index,contact,About_us,signup
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path("", index, name="home"),
    path('contact/', contact),
    path('about/',About_us),
    path("signup/",signup,name="signup"),
    path('inbox/',include('conversation.urls')),
    path("login/",auth_views.LoginView.as_view(authentication_form=LoginForm,template_name="item/login.html"),name="login"),
    path("logout/",LogoutView.as_view(next_page=reverse_lazy("login")),name="logout")]