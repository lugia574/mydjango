from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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
        # return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})
        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:

        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})

class AccountCreateView(CreateView):
    model = User # 유저 장고 디폴트 모델
    form_class = UserCreationForm # 회원가입 폼
    success_url = reverse_lazy('accountapp:hello_world') # 저장 되어 있다가 호출 될때 값을 줘야 해서 reverse 랑 방식이 다름 그래서 _lazy를 쓰는거야
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name ='target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:update.html')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
