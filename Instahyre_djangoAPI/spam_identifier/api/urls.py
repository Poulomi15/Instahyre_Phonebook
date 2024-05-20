from django.urls import path
from .views import RegisterView, LoginView, ContactListView, ContactDetailView, SearchView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('search/', SearchView.as_view(), name='search'),
]
