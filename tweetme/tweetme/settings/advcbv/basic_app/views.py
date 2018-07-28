from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,
                                UpdateView,DeleteView)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from . import models

class IndexView(TemplateView):
    template_name='basic_app/index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context={'insert_me':'Hello!!'}
        return context

class SchoolListView(ListView):

    model=models.School
    template_name='basic_app_1/school_list.html'
    context_object_name='schools'
    #returns name school_list automatically

class SchoolDetailedView(DetailView):
    context_object_name="school_detail"
    model=models.School
    template_name='basic_app_1/school_detail.html'

class SchoolCreateView(CreateView):
    template_name="basic_app_1/school_form.html"
    fields = ('name','principal','location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School
    template_name='basic_app_1/school_form.html'

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy("basic_app_1:list")
    template_name='basic_app_1/school_confirm_delete.html'
