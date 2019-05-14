from django.shortcuts import render
from news.models import *

def novelty(request, novelty_id):
    news_plural = News.objects.get(id=novelty_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'news/novelty.html', locals())