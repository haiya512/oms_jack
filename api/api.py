# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
# from models import GroupList, HostGroup, HostList, IdcAsset


def my_render(template, data, request):
    return render_to_response(template, data, context_instance=RequestContext(request))

def httperror(request, emg):
    message = emg
    return render_to_response('error.html', locals())