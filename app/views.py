from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='husband')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='husband')
    QSW=Webpage.objects.exclude(topic_name='wife')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='wife').order_by('-name')    
    QSW=Webpage.objects.all().order_by(Length('name'))    
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    
    QSW=Webpage.objects.filter(name__startswith='D')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='d')    
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    QSW=Webpage.objects.filter(name__in=['vandana','dinesh','meghan'])
    QSW=Webpage.objects.filter(Q(topic_name='husband') | Q(name='meghan'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Q(topic_name='pavani') & Q(url__startswith='https'))
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
def display_access(request):
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='1998-08-10')    
    QSA=AccessRecords.objects.filter(date__gt='1998-08-10')    
    QSA=AccessRecords.objects.filter(date__gte='1998-08-10') 
    QSA=AccessRecords.objects.filter(date__lte='1998-08-10')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='1998')  
    QSA=AccessRecords.objects.filter(date__month='8')    
    QSA=AccessRecords.objects.filter(date__day='10')   
    QSA=AccessRecords.objects.filter(date__year__gt='1998')
    d={'access':QSA}
    return render(request,'display_access.html',d)


def update_webpage(request):
    Webpage.objects.filter(name='dinesh123').update(url='https://dinesh.com')
    Webpage.objects.filter(topic_name='wife').update(name='xwife')
    Webpage.objects.filter(name='sandhya').update(topic_name='friend')
    Webpage.objects.filter(name='pavani').update(topic_name='schoolmate')
    Webpage.objects.update_or_create(name='vandana',defaults={'url':'https://vandana.com'})
    Webpage.objects.update_or_create(name='dinesh',defaults={'url':'https://dinesh.com'})
    T=Topic.objects.get_or_create(topic_name='bestfriend')[0]
    T.save()
    Webpage.objects.update_or_create(name='ashu',defaults={'topic_name':T,'url':'https://dinesh.com'})

    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def delete_webpage(request):
    Webpage.objects.filter(name='vandana').delete()
   # Webpage.objects.all().delete()
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)







