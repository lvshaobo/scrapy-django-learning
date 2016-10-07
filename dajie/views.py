from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Direction


class DetailView(generic.DetailView):
    model = Direction
    template_name = 'dajie/detail.html'


class IndexView(generic.ListView):
    template_name = 'dajie/index.html'
    context_object_name = 'highest_salary_list'

    def get_queryset(self):
        """Return the five salary-highest job_title."""
        return Direction.objects.order_by('-salary')[:5]

