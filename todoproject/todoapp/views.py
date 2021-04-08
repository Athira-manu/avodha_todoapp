from django.shortcuts import render,redirect
from . models import task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def add(request):
#
#     return render(request,"task.html")

class TaskListView(ListView):
    model = task
    template_name = 'taskview.html'
    context_object_name = 'result'

class TaskDetailView(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 't'
    fields= ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    def get_success_url(self):
        return reverse_lazy('cbvtask')
def fun(request):
    ob=task.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        priority=request.POST.get("priority")
        date=request.POST.get("date")
        obj=task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,"taskview.html",{'result':ob})
def delete(request,taskid):
    ob1=task.objects.get(id=taskid)
    if request.method=="POST":
        ob1.delete()
        return redirect('/')
    return render(request,"delete.html",{'ob1':ob1})
def update(request,id):
    ob2=task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=ob2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'a':ob2,'b':form})

