from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    print "INDEX VIEW!"
    courses = models.Course.objects.all()
    print courses
    context = {'courses': courses}
    return render(request, 'coursesapp/index.html', context)


def confirm(request, id):
    print "CONFIRM VIEW!"
    course = models.Course.objects.get(id=id)
    print course.name
    context = {'course': course}
    return render(request, 'coursesapp/confirm.html', context)


def destroy(request, id):
    print "DESTROY VIEW!"
    print request.POST
    if request.POST.has_key('no'):
        return redirect('/')
    elif request.POST.has_key('yes'):
        models.Course.objects.filter(id=id).delete()
        return redirect('/')


def add(request):
    # print "NAME: ", request.POST('name'), "DESCRIPTION: ", request.POST('description')
    models.Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')
