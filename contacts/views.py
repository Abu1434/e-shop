from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from contacts.forms import ContactModelForm


class ContactListView(TemplateView):
    template_name = 'contact.html'


class ContactCreateView(CreateView):
    form_class = ContactModelForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contacts:list')

