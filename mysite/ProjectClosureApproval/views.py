from django.shortcuts import render
from django.http import *
from WorkOrderEscalation.models import WorkOrderEscalation
from django.shortcuts import redirect

def ClosureApproval(request):
    dict_teams = {}
    P = WorkOrderEscalation.objects.all()
    params = {'data': P}
    if request.method == 'POST':
        list_teams = request.POST.getlist('team')
        print(list_teams)
        dict_teams['Teams'] = list_teams
        return render(request,'OutlookEsc.html',dict_teams)
    else:
        return render(request, 'ClosureApproval.html', params)




# Create your views here.
