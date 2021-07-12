from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld




def hello_world (request):
    # 라우팅 해줘야해 (연결)
    # 메인 앱에서 먼저 받고 여기로 보냄

    if request.method == 'POST': # 기본적으로 겟 방식으로 작동함
        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()

        # data_list = HelloWorld.objects.all()
        # return render(request, 'account/hello_world.html', context={'data_list': data_list})
        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:

        data_list = HelloWorld.objects.all()
        return render(request, 'account/hello_world.html', context={'data_list': data_list})
