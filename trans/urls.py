from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.gethome,name="home"),
    path('login/',views.SiteLogin.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="home"),name="logout"),
    path('award/',views.getAward,name="award"),
    path('approve/',views.getApprove,name="approve"),
    path('deleteForm/<int:id>/<str:email>',views.deleteForm),
    # path('testSendMail/<int:id>',views.testSendMail),
    path('testSendMail/<int:id>/<str:email>',views.testSendMail),
]
