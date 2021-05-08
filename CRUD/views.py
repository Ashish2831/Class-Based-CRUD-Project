from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView, View
from django.contrib import messages
from .forms import *

# Create your views here.
class Index(TemplateView):
    template_name = 'CRUD/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        st = Student_Form()
        stu = Student.objects.all()
        context['st'] = st
        context['all'] = stu
        return context

    def post(self, request):
        form = Student_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added Successfully!!")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'CRUD/index.html', {'st' : form})

class Update(View):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        form = Student_Form(instance=student)
        return render(request, 'CRUD/update.html', {'st' : form})

    def post(self, request, id):
        student = Student.objects.get(pk=id)
        form = Student_Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Updated Successfully!!")
            return render(request, 'CRUD/update.html', {'st' : form})
        else:
            return render(request, 'CRUD/update.html', {'st' : form})

class Delete(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        messages.success(request, "Student Deleted Successfully!!")
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        student = Student.objects.get(pk=kwargs['id'])
        student.delete()
        return super().get_redirect_url(*args, **kwargs)