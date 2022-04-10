from django import template
# from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import DoctorVisitsForm, FamilyVisitsForm, MedicineForm, TripsForm, TakeoutsForm
from .models import DoctorVisit, FamilyVisit, MedicineList, Takeouts, Trips


@login_required(login_url="/login/")
def index(request):
    visits = DoctorVisit.objects.filter(user=request.user.id)[1::]
    context = {'segment': 'index'}
    print(visits)

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        context = {}
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        # elif load_template == 'doctors':
        #     return HttpResponseRedirect(reverse('doctors:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))


def doctor_visits(request):
    form = DoctorVisitsForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    submitted = False
    visits = DoctorVisit.objects.filter(user=request.user.id)
    if request.method == "POST":
        print(form.errors, form.is_valid())
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
        else:
            form = DoctorVisitsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'visits': visits,
    }
    return HttpResponse(html_template.render(context, request))


def family_visits(request):
    form = FamilyVisitsForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    visits = FamilyVisit.objects.filter(user=request.user.id)
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
            # form.save()
        else:
            form = FamilyVisitsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'visits': visits,

    }
    return HttpResponse(html_template.render(context, request))


def medicine(request):
    form = MedicineForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    lists = MedicineList.objects.filter(user=request.user.id)
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
            # form.save()
        else:
            form = MedicineForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'lists': lists,
    }
    return HttpResponse(html_template.render(context, request))


def trips(request):
    form = TripsForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    trips = Trips.objects.filter(user=request.user.id)
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
            # form.save()
        else:
            form = TripsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'trips': trips,
    }
    return HttpResponse(html_template.render(context, request))


def takeouts(request):
    form = TakeoutsForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    outs = Takeouts.objects.filter(user=request.user.id)
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
            # form.save()
        else:
            form = TakeoutsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'outs': outs
    }
    return HttpResponse(html_template.render(context, request))
