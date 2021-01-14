from django.shortcuts import render,redirect
from . models import TdList
from . form import TdForm
# Create your views here.
def list_view(request):
    lists = TdList.objects.all()
    return render (request,'list.html',{'lists':lists})



def td_write(request):
    if request.method == 'POST':
        form = TdForm(request.POST)
        form.save()
        return redirect ('list_view')
    else:
        form = TdForm()
    return render(request,'add.html',{'form':form})

