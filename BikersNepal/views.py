from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Bikes.models import UploadDetails


def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    else:

        uploaded_image = request.FILES['image']

        fssobj = FileSystemStorage()
        filename = fssobj.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fssobj.url(filename)

        bikeobj = UploadDetails(file=uploaded_image_url,
                                Bikename=request.POST.get('Bike_name', "Upcomming Bike"),
                                EngineDisplacement=request.POST.get('Engine_Displacement', 30),
                                maxpower=request.POST.get('max_power', 25),
                                maxtorque=request.POST.get('max_torque', 20),
                                Fuel=request.POST.get('fuel', "Not Set"),
                                Company=request.POST.get('company', ""),
                                Gear=request.POST.get('gear', 5),
                                Price=request.POST.get('price', 200000),
                                Desc=request.POST.get('desc', "Nice Bike"),

                                )
        bikeobj.save()

        return HttpResponse(
            '<a href="/index/">Return back to homepage</a><br>'
            '<a href="/upload/">Upload more</a><br>'
            ' <h1>You have successfully uploaded an image</h1>')


def honda(request):
    if request.method == "GET":
        Bike_list = UploadDetails.objects.all().filter(Company='Honda')

        context_variable = {
            'detail': Bike_list
        }

        print(context_variable)
        return render(request, 'Honda.html', context_variable)


def yamaha(request):
    if request.method == "GET":
        Bike_list = UploadDetails.objects.all().filter(Company='Yamaha')

        context_variable = {
            'detail': Bike_list
        }

        print(context_variable)
        return render(request, 'Yamaha.html', context_variable)


def pulsar(request):
    if request.method == "GET":
        Bike_list = UploadDetails.objects.all().filter(Company='Bajaj')

        context_variable = {
            'detail': Bike_list
        }

        print(context_variable)
        return render(request, 'Bajaj.html', context_variable)


def suzuki(request):
    if request.method == "GET":
        Bike_list = UploadDetails.objects.all().filter(Company='Suzuki')

        context_variable = {
            'detail': Bike_list
        }

        print(context_variable)
        return render(request, 'Suzuki.html', context_variable)


def index(request):
    if request.method == "GET":
        Bike_list = UploadDetails.objects.all()

        context_variable = {
            'detail': Bike_list
        }

        print(context_variable)
        return render(request, 'index.html', context_variable)


@permission_required('Bikes.delete_uploaddetails', login_url='/restricted/')
def delete(request, pk):
    list = UploadDetails.objects.get(pk=pk)
    list.delete()
    return redirect("/Honda/")


@permission_required('Bikes.delete_uploaddetails', login_url='/restricted/')
def deleteb(request, pk):
    list = UploadDetails.objects.get(pk=pk)
    list.delete()
    return redirect("/Bajaj/")


@permission_required('Bikes.delete_uploaddetails', login_url='/restricted/')
def deletes(request, pk):
    list = UploadDetails.objects.get(pk=pk)
    list.delete()
    return redirect("/Suzuki/")


@permission_required('Bikes.delete_uploaddetails', login_url='/restricted/')
def deletey(request, pk):
    list = UploadDetails.objects.get(pk=pk)
    list.delete()
    return redirect("/Yamaha/")


@permission_required('Bikes.change_uploaddetails', login_url='/restricted/')
def update_form(request, pk):
    bikwobj = UploadDetails.objects.get(pk=pk)
    return render(request, 'edit.html', {'bike': bikwobj})


@permission_required('Bikes.change_uploaddetails', login_url='/restricted/')
def update(request, pk):
    edit = UploadDetails.objects.get(pk=pk)
    if request.method == "POST":
        uploaded_image = request.FILES['image']

        fssobj = FileSystemStorage()
        filename = fssobj.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fssobj.url(filename)

        edit.Bikename = request.POST.get('Bike_name')
        edit.EngineDisplacement = request.POST.get('Engine_Displacement', '')
        edit.maxpower = request.POST.get('max_power', '')
        edit.maxtorque = request.POST.get('max_torque', '')
        edit.Fuel = request.POST.get('fuel', '')
        edit.Company = request.POST.get('company', '')
        edit.Gear = request.POST.get('gear', )
        edit.Price = request.POST.get('price', )
        edit.Desc = request.POST.get('description', '')
        edit.file = uploaded_image_url

        edit.save()
        company = request.POST.get('company', 'index')

        if company == "Suzuki":
            return redirect("/Suzuki/")
        elif company == "Honda":
            return redirect("/Honda/")
        elif company == "Yamaha":
            return redirect("/Yamaha/")
        elif company == "Bajaj":
            return redirect("/Bajaj/")
        else:
            return redirect("/index/")


def logout_view(request):
    logout(request)
    return HttpResponse(
        '<h2> Successfully logged out from the Bikers Nepal</h2><br><br><br><a href="http://127.0.0.1:8000/signupform/signin/"><h1>Login Again</h1></a>')


def home_restricted(request):
    return render(request, 'Restricted.html')


def aboutus(request):
    return render(request, 'aboutus.html')
