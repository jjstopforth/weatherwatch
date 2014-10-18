from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
  context = RequestContext(request)

  context_dict = {'boldmessage':'This is what I wanted bold'}

  return render_to_response('weatherwatch/index.html', context_dict, context)

def about(request):

  return render_to_response('weatherwatch/about.html', {}, RequestContext(request))
