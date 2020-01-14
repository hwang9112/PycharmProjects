from django.shortcuts import render
from feedback.models import *
from datetime import datetime

def index(request):
    msg = 'My Message Test'
    return render(request, 'home/index.html', {'message': msg})


    # # Feedback 객체 생성
    # fb = Feedback(name='Kim', email='kim@test.com', comment='Hi', createDate=datetime.now())
    #
    # # 새 객체 INSERT
    # fb.save()

    for f in Feedback.objects.all():
        s += str(f.id) + ' : ' + f.name + '\n'


    return render(request, 'home/index.html', {'s': s})

