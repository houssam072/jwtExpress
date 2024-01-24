from django.urls import path
from .views import RegisterView, RetrieveUserView

app_name = 'users'
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view())
]