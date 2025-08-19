from django.shortcuts import render
from myapp.models import Entry

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/entry_list.html', {'entries': entries})