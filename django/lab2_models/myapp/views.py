from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Entry, Author
from django import forms

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['headline', 'body_text', 'pub_date', 'blog', 'authors']

def entry_list(request):
    entries = Entry.objects.all()
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:entry_list')
    return render(request, 'myapp/entry_list.html', {'entries': entries, 'form': form})


def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.delete()
    return redirect('myapp:entry_list')

def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'myapp/entry_detail.html', {'entry': entry})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    entries = author.entry_set.all()
    return render(request, 'myapp/author_detail.html', {'author': author, 'entries': entries})