from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import DoctorVisitsForm, FamilyVisitsForm, MedicineForm, TripsForm, TakeoutsForm
from .models import DoctorVisit, FamilyVisit, MedicineList, Takeouts, Trips


@login_required(login_url="/login/")
def index(request):
    visits = DoctorVisit.objects.filter(user=request.user.id)
    fams = FamilyVisit.objects.filter(user=request.user.id)
    meds = MedicineList.objects.filter(user=request.user.id)
    trips = Trips.objects.filter(user=request.user.id)
    outs = Takeouts.objects.filter(user=request.user.id)
    context = {'segment': 'index', 'visits': visits,
               'lists': meds, 'visits': fams, 'trips': trips, 'outs': outs, }

    html_template = loader.get_template('home/index.html')
    print(visits, fams, meds, trips, outs)
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
            form = DoctorVisitsForm
        else:
            form = DoctorVisitsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'visits': visits,
        'segment': 'doctors',
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
            form = FamilyVisitsForm
        else:
            form = FamilyVisitsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'visits': visits,
        'segment': 'family',

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
            form = MedicineForm
        else:
            form = MedicineForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'lists': lists,
        'segment': 'medicines'
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
            form = TripsForm
        else:
            form = TripsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'trips': trips,
        'segment': 'trips',
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
            form = TakeoutsForm
        else:
            form = TakeoutsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'outs': outs,
        'segment': 'takeouts'
    }
    return HttpResponse(html_template.render(context, request))
