from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views import generic
import queen_app.queen as queen_lib
from queen_app.models import Desk


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'queen_app/login.html', {'form': form})


def index(request):
    if (request.GET.get('work')):
        print("button")
        queen = queen_lib.QueenClass(8)
        queen.find(0,0)

        all_desk = []
        for solution in queen.all_solution:
            one_desk = Desk()
            one_desk.set_rank(solution)
            all_desk.append(one_desk)

        Desk.objects.bulk_create(all_desk, ignore_conflicts=True)
        #queen.all_solution[0]
    desk = Desk.objects.all()
    return render(request, 'queen_app/detail.html', {'desk': desk})
