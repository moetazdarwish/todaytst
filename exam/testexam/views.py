import decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from testinv.models import Person
from django.views.decorators.csrf import csrf_exempt

from testexam.models import Person


def testform(request):
    if request.POST:
        name = request.POST.get('name')
        age = request.POST.get('age')
        nationalityID = request.POST.get('nationalityID')
        date = request.POST.get('birthDate')
        print(age)
        age2 = decimal.Decimal(age)
        print(age2)
        Person.objects.create(name=name,age=age,nationalityID=nationalityID,birthDate=date)

    data = Person.objects.all()
    context = {'data':data}
    return render(request,'home.html',context=context)

def deltestform(request,pk):
    print(pk)
    Person.objects.get(id=pk).delete()
    data = Person.objects.all()
    context = {'data': data}
    return render(request, 'home.html', context=context)
@csrf_exempt
def search(request):
    print('search')
    nationalityID = request.POST.get('nationalityID')
    data = Person.objects.filter(nationalityID__icontains=nationalityID)
    fnl_data = []
    for i in data:
        dlt={
            'name':i.name,
            'age':i.age,
            'nationalityID':i.nationalityID,
            'birthDate':i.birthDate,
        }
        fnl_data.append(dlt)

    return HttpResponse(fnl_data)