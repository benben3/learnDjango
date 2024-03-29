from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

from .models import Quote
from .forms import QuoteForm
from pages.models import Page

def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'quotes/quote.html', {'form': form, 'page_list': Page.objects.all(),
    'submitted': submitted})

# Create your views here.
