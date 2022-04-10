from django.urls import path, include



from . import views

urlpatterns = [ 
   path('', views.MessageView.as_view(), name="messages"),
   path('account/', include("django.contrib.auth.urls")),
   path('signup/', views.SignUp.as_view(), name="signup"),
   path('logout/', views.logout_request, name="logout"),
]