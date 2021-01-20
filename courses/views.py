from django.shortcuts import render
from .models import Course,VideoRepo,Review
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

def coursedirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['webdev'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def businessdirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['business'])
        f = 'Business'
        return render(request, 'courses/courses-list.html',{'c': c,'f':f})
    else:
        c = Course.objects.filter(field='Business')
        f = 'Business'
        return render(request, 'courses/courses-list.html', {'c': c,'f':f})


def mobiledirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['app'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def itdirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['it'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def archidirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['architecture'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def marketingdirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['marketing'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def lifestyledirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['lifestyle'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def photographydirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['photography'])
        return render(request, 'courses/courses-list.html', {'c': c})
    else:
        return render(request, 'courses/episode.html')


def fitnessdirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['fitness'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def musicdirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['music'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def edirect(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['ecommerce'])
        return render(request, 'courses/courses-list.html',{'c': c})
    else:
        return render(request, 'courses/episode.html')


def courseintro(request):
    if request.method == 'POST':
        cou = request.POST['course']
        co = Course.objects.get(id=cou)
        re = Review.objects.filter(course=co)
        return render(request, 'courses/course-resume.html',{'co': co,'re':re})
    else:
        return render(request, 'courses/course-list.html')


def newsort(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['field']).order_by('-id')
        return render(request, 'courses/courses-list.html', {'c': c})
    else:
        return render(request, 'courses/course-list.html')


def intermediatesort(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['field3'],level='Intermediate')
        return render(request, 'courses/courses-list.html', {'c': c})
    else:
        return render(request, 'courses/course-list.html')


def advancedsort(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['field4'], level='Advanced')
        return render(request, 'courses/courses-list.html', {'c': c})
    else:
        return render(request, 'courses/course-list.html')


def beginnersort(request):
    if request.method == 'POST':
        c = Course.objects.filter(field=request.POST['field2'], level='Beginner')
        return render(request, 'courses/courses-list.html', {'c': c})
    else:
        c = Course.objects.filter(field=request.POST['field2'], level='Beginner')
        return render(request, 'courses/courses-list.html', {'c': c})


def wupload(request):
    if request.method == 'POST':
        name = request.POST['title']
        field = request.POST['category']
        topic = request.POST['topic']
        desc = request.POST['short_description']
        tbl = request.POST['tbl']
        req = request.POST['requirements']
        instructor = User.objects.get(username=request.user.get_username())
        level = request.POST['level']
        vid1name = request.POST['vid1name']
        vid1src = request.FILES['vid1']
        fs = FileSystemStorage()
        file = fs.save(vid1src.name, vid1src)
        c = Course(name=name,field=field,topic=topic,description=desc,ToBeLearned=tbl,requirements=req,
                   instructor=instructor,level=level)
        c.save()
        v = VideoRepo(videoname=vid1name,videosrc=file,course=Course.objects.get(name=name,instructor=instructor))
        v.save()
        m = 'course added'
        return render(request, 'courses/add-course.html',{'m':m})
    else:
        return render(request, 'courses/add-course.html')


def viewcourse(request):
    c = Course.objects.filter(field='Web Development')
    m = Course.objects.filter(field='Mobile App')
    b = Course.objects.filter(field='Business')
    it = Course.objects.filter(field='IT Software')
    ma = Course.objects.filter(field='Marketing')
    l = Course.objects.filter(field='Lifestyle')
    a = Course.objects.filter(field='Architecture')
    p = Course.objects.filter(field='Photography')
    mu = Course.objects.filter(field='Music')
    e = Course.objects.filter(field='Ecommerce')

    return render(request, 'courses/episode.html',{'c': c, 'm': m, 'b': b, 'it': it, 'ma': ma, 'l': l,
                                                   'a': a, 'p': p, 'mu': mu, 'e': e})


def review(request):
    if request.method == 'POST':
        name = request.POST['name']
        rev = request.POST['review']
        cou = request.POST['course']
        ins = request.POST['instructor']
        co = Course.objects.get(name=cou,instructor=ins)
        us = User.objects.get(username=ins)
        rv = User.objects.get(username=name)
        r = Review(review=rev,course=co,reviewed_by=rv,instructor=us)
        r.save()
    else:
        return render(request, 'courses/course-resume.html')


def listcourse(request):
    if request.method == 'POST':
        name = request.POST['cou']
        ins = request.POST['ins']
        us = User.objects.get(username=ins)
        co = Course.objects.get(name=name, instructor=us)
        cour = VideoRepo.objects.filter(course=co).order_by('-id')
        return render(request, 'courses/viewcourse.html', {'cour': cour , 'cv':co})
    else:
        return render(request, 'courses/course-resume.html')


def playcourse(request):
    if request.method == 'POST':
        name = request.POST['vid']
        cv = request.POST['co']
        n = VideoRepo.objects.get(id=name)
        co = Course.objects.get(id=cv)
        cour = VideoRepo.objects.filter(course=co).order_by('-id')
        return render(request, 'courses/viewcourse.html',{'n': n , 'cour': cour})
    else:
        return render(request, 'courses/viewcourse.html')


def check(request):
    return render(request, 'courses/check.html')