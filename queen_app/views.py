from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic
import queen_app.queen as queen_lib
from queen_app.models import Desk


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
