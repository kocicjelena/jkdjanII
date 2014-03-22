from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader

def index(request):
    return HttpResponse("<a href='blog/posts'>Blog</a>")
def index2(request):
    return HttpResponse("<a href='blog/posts'>Blog</a>")

	