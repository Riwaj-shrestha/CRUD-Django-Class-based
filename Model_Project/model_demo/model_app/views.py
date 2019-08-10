from django.shortcuts import render
from model_app.models import Books
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class IndexView(ListView):
    template_name='model_app/index.html'
    context_object_name = 'book_list'
    model = Books

class BookDetailView(DetailView):
    template_name='model_app/detail.html'
    context_object_name = 'book'
    model = Books

class BookCreateView(CreateView):
    model = Books
    fields = ['title','rate', 'quantity']
    

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid

class BookDeleteView(DeleteView):
    model = Books
    success_url = '/'

class BookUpdateView(UpdateView):
    model = Books
    fields = ['title','rate', 'quantity']