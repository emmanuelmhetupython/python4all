from django.urls import path
from .import views

app_name="main"

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path('whatwedo',views.whatwedo, name="whatwedo"),
    path('categories',views.forum, name="forum"),
    path('register',views.register,name="register"),
    path('blog',views.homepage,name="blog"),
    path('logout',views.logout_request, name="logout"),
    path('login',views.login_request, name="logout"),
    path('contactus',views.contactus, name="contactus"),
    path('csscode',views.csscode, name="csscode"),  
    path('aboutMI',views.aboutMI, name="aboutMI"),  
    path('menu',views.menu, name="menu"),  
    path('index',views.index, name="index"), 
    path('donate',views.donate,name="donate"),
    path('shop',views.shop,name="shop"),
    path('hireme',views.hireme,name="hireme"),
    # views.register redirects the url to the register view
]

