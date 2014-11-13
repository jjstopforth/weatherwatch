from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
  context = RequestContext(request)

  context_dict = {'boldmessage':'Hi Joan! :)'}

  return render_to_response('weatherwatch/index.html', context_dict, context)

def about(request):

    context = RequestContext(request)

    #quick fibonacci
    a = 1
    b = 1
    c = a+b

    n = 0

    fib_string = ''

    while n < 10:

        fib_string += ' ' + str(a)

        a = b
        b = c
        c = a+b

        n += 1

    var_dict = {'fib' : fib_string, 'n' : n }

    return render_to_response('weatherwatch/about.html', var_dict, RequestContext(request))
