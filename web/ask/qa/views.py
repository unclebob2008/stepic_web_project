from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

def app(request, *args, **kwargs):
    return HttpResponse('OK')

def topnew(request):
    limit = 10
    page = request.GET.get('page', 1)
    posts = Question.objects.new()
    paginator = Paginator(posts, limit)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)
    return render(request, 'new.html', {'posts': qs})

def toppop(request):
    limit = 10
    page = request.GET.get('page', 1)
    posts = Question.objects.popular()
    paginator = Paginator(posts, limit)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)
    return render(request, 'new.html', {'posts': qs})

def quone(request, *args, **kwargs):
    qid = args[0]
    try:
        q = Question.objects.get(pk=qid)
        ans = Answer.objects.filter(question__pk=qid)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'quone.html', {'title': q.title, 'text': q.text, 'ans': ans})
