#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse,Http404
import datetime
def hello(request):
    return HttpResponse('Hello world')

def get_date(request):
    now =datetime.datetime.now()
    html='It is now %s'% now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except:
        raise Http404()

    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="In %s hour(s), it will be %s ."%(offset,dt)
    return HttpResponse(html)