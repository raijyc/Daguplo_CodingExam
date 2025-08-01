from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def membership(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))