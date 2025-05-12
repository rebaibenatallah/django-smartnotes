from django.shortcuts import render
from django.http import HttpResponse
from .models import poll,poll_option,voters

# Create your views here.
def index(request):
    title = request.POST.get('title')
    description = request.POST.get('Description')
    duration = request.POST.get('Duration')
    poll_option_1 = request.POST.get('poll_option_1')
    poll_option_2 = request.POST.get('poll_option_2')
    # print(title ,description , duration)
    data = poll(title = title,description=description,duration=duration)
    # print(next_id)
    if(request.POST):
        data.save()
        next_id = poll.objects.order_by('-id').first()
        data2= poll_option(text=poll_option_2,Id_poll=next_id)
        data1= poll_option(text=poll_option_1,Id_poll=next_id)
        data1.save()
        data2.save()
    
    context = {'poll': poll.objects.all(),'poll_options': poll_option.objects.all(),'voter':voters.objects.all()}
    return render(request , 'polls/index.html',context)
