from django.shortcuts import render
from django.http import HttpResponse
from .models import poll,poll_option,voters

# Create your views here.
def index(request):
    context = {'poll': poll.objects.all(),'poll_options': poll_option.objects.filter(Id_poll=1),'voter':voters.objects.all()}
    return render(request , 'polls/index.html',context)
