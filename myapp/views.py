from django.shortcuts import render,redirect
from myapp.form import LibraryForm
from myapp.models import Library
from django.views.generic import View,ListView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy

class LibraryListView(ListView):
    model=Library
    template_name="lib-list.html"
    context_object_name="books"

class LibraryCreateView(CreateView):
    model=Library
    form_class=LibraryForm
    template_name="lib-create.html"
    success_url=reverse_lazy("list")

class LibraryUpdateView(UpdateView):
    model=Library
    form_class=LibraryForm
    template_name="lib-update.html"
    success_url=reverse_lazy("list")

class LibraryDetailView(DetailView):
    model=Library
    template_name="lib-detail.html"
    context_object_name="book"

class LibraryDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Library.objects.get(id=id).delete()
        return redirect("list")

