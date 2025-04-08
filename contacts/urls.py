from django.urls import path

from contacts.views import ContactListView, ContactCreateView

app_name = 'contacts'

urlpatterns = [
    path('', ContactListView.as_view(), name='list'),
    path('contact/', ContactCreateView.as_view(), name='create'),
]
