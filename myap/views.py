from django.shortcuts import render,HttpResponse,redirect
from . models import Details
from django.contrib import messages


# Create your views here.
def index(request):
    details=Details.objects.all()
    if request.method == 'POST':

        new = Details(name=request.POST['name'])
        new.save()
        messages.info(request, 'Added')
        return redirect('/')

    return render(request,'index.html',{'detail':details})

def delete(request , details_id):
    d_id = Details.objects.get(id=details_id)
    d_id.delete()
    messages.info(request, 'deleted', extra_tags='delete')
    return redirect('/')








