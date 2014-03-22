from django.shortcuts import render, render_to_response
from .models import Blog, Author, Entry
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Blog
from django.http import HttpResponse
from django.views.generic import View
class MyView(View):
    greeting = "Good Day"
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
class BookListView(ListView):
    model = Blog

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('pub_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response
class AboutView(TemplateView):
    template_name = "about.html"
def posts(request):
    ent = Blog.objects.all()[:10]
    return render(request, 'index.html', {'posts' : ent})
def searchform(request):
    return render(request, 'search_form2.html')
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Blog.objects.filter(name=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})
def i(request):
    errors = []
    if 'q' and 'b' in request.GET:
        q = request.GET['q']
        b = request.GET['b']
        if not q and not b:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            blog = Blog.objects.create(name=q, tagline=b)
            blog.save()
            return render(request, 'print.html',
                {'blog': blog, 'query': q})
    return render(request, 'input.html',
        {'errors': errors})