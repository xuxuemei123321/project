from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext
import time
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'overview/index.html')