from django.urls import path
from .views import SignView

urlpatterns = [
    path('signup/', SignView.as_view(), name='signup'),
]