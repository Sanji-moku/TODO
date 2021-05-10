from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from apptodo.models import Task
from apptodo.forms import TaskForm
# Create your views here.


def todoHome(request):
    tasks = Task.objects.all().order_by('done')

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            print(form)
            return redirect(reverse('todo-home'))
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form':form,
    }
    return render(request,'apptodo/home.html',context)


def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(reverse('todo-home'))


def doneTask(request, id):
    task = Task.objects.get(id=id)
    if task.done == False:
        task.done = True
        task.save()
    else:
        task.done = False
        task.save()
    return redirect(reverse('todo-home'))


def deleteAllDone(request):
    all_done = Task.objects.filter(done=True)
    all_done.delete()
    return redirect(reverse('todo-home'))