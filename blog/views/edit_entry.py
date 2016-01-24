from django import forms
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import BlogEntry


class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ('title', 'content')


def create(request):
    entry = BlogEntry()
    entry.save()
    return redirect(reverse('edit', args=(entry.id,) ))


def edit(request, entry_id):
    entry = get_object_or_404(BlogEntry, id=entry_id)
    form = EntryForm(request.POST or None, instance=entry)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('entry', args=(entry.id,) ))

    return render(request, 'edit_entry.html', {'form': form})

