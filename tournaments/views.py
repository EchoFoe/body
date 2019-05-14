from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from tournaments.models import *
# from utils.uploadings import UploadingProducts
# from django.contrib import messages

def tournament(request, tournament_id):
    tournaments = Tournaments.objects.get(id=tournament_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'tournaments/tournaments.html', locals())