# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .forms import SearchForm
from .models import Book, Classifier, Technology
from array import *

@login_required(login_url="/login/")
def index(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if (form.cleaned_data['parametr'] == 'id_doc'):
                info = 'Результат поиска по параметру "Код документа"'
                docs = Book.objects.filter(id_doc__contains=form.cleaned_data['value'])
                if (len(docs) == 0):
                    info = 'Результат поиска по параметру "Код документа" не дал результатов'
            elif (form.cleaned_data['parametr'] == 'autor'):
                info = 'Результат поиска по параметру "Автор документа"'
                docs = Book.objects.filter(autor__contains=form.cleaned_data['value'])
                if (len(docs) == 0):
                    info = 'Результат поиска по параметру "Автор документа" не дал результатов'
            elif (form.cleaned_data['parametr'] == 'isbn'):
                info = 'Результат поиска по параметру "ISBN документа"'
                docs = Book.objects.filter(isbn__contains=form.cleaned_data['value'])
                if (len(docs) == 0):
                    info = 'Результат поиска по параметру "ISBN документа" не дал результатов'
            elif (form.cleaned_data['parametr'] == 'short_name'):
                info = 'Результат поиска по параметру "Название документа"'
                docs = Book.objects.filter(short_name__contains=form.cleaned_data['value'])
                if (len(docs) == 0):
                    info = 'Результат поиска по параметру "Название документа" не дал результатов'
            else:
                info = 'Ошибка поиска'
            return render(request, 'docs/search.html', {'docs': docs, 'info': info})
    else:
        form = SearchForm()

    classifier = Classifier.objects.all()
    technology = Technology.objects.all()

    amount = array('i', [0])
    for el in classifier:
        amount.insert(len(amount), Book.objects.filter(classifier_doc__name__contains=el.name).count())

    context = {
        'segment': 'index',
        'classifier': classifier,
        'amount': amount,
        'technology': technology,
        'form': form,
    }

    html_template = loader.get_template('home/index.html')

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))


        context['segment'] = load_template


        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def docs(request):
    docs = Book.objects.order_by('id')
    return render(request, 'docs/docs.html', {'docs': docs})

def cabinet(request):
    return render(request, 'accounts/cabinet.html')

def classifier_view(request, classifier_doc):
    docs = Book.objects.filter(classifier_doc__name__contains=classifier_doc)
    return render(request, 'docs/classifier.html', {'docs': docs, 'info': classifier_doc})

def technology_view(request, technology_doc):
    docs = Book.objects.filter(classifier_doc__name__contains=technology_doc)
    return render(request, 'docs/technology.html', {'docs': docs, 'info': technology_doc})

def search_docs(request, parametr, value):
    if (parametr == 'id_doc'):
        info = 'Результат поиска по параметру "Код документа"'
        docs = Book.objects.filter(id_doc__contains=value)
    elif (parametr == 'autor'):
        info = 'Результат поиска по параметру "Автор документа"'
        docs = Book.objects.filter(autor__contains=value)
    elif (parametr == 'isbn'):
        info = 'Результат поиска по параметру "ISBN документа"'
        docs = Book.objects.filter(isbn__contains=value)
    elif (parametr == 'short_name'):
        info = 'Результат поиска по параметру "Название документа"'
        docs = Book.objects.filter(short_name__contains=value)
    return render(request, 'docs/search.html', {'docs': docs, 'info': info})