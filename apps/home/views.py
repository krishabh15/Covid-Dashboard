from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import DoctorVisitsForm, FamilyVisitsForm, MedicineForm, TripsForm, TakeoutsForm, TempDataForm, PersonalDataForm
from .models import DoctorVisit, FamilyVisit, MedicineList, PersonalData, Takeouts, TempData, Trips


@login_required(login_url="/login/")
def index(request):
    user = request.user.id
    visits = DoctorVisit.objects.filter(user=user).order_by('-visit_date')
    fams = FamilyVisit.objects.filter(user=user)
    meds = MedicineList.objects.filter(user=user)
    trips = Trips.objects.filter(user=user)
    outs = Takeouts.objects.filter(user=user)
    temps = TempData.objects.filter(user=user)
    temp = TempData.objects.filter(user=user).last()
    takeout = Takeouts.objects.filter(user=user).last()
    drvisit = DoctorVisit.objects.filter(user=user).last()
    if(temp is not None):
        temp = int(temp.temp)
    context = {'segment': 'index', 'visits': visits,
               'lists': meds, 'visits': fams,
               'trips': trips, 'outs': outs,
               'temps': temps, 'temp': temp,
               'takeout': takeout, 'drvisit': drvisit}

    html_template = loader.get_template('home/index.html')
    print(type(temp))
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


def personal_data(request):
    form = PersonalDataForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    outs = PersonalData.objects.filter(user=request.user.id)
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
            form = PersonalDataForm
        else:
            form = PersonalDataForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'outs': outs,
        'segment': 'personal_data',
    }
    return HttpResponse(html_template.render(context, request))


def temp_data(request):
    form = TempDataForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    temps = TempData.objects.filter(user=request.user.id)
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.user = request.user.id  # logged in user
            venue.save()
            submitted = True
            form = TempDataForm
        else:
            form = TempDataForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
        'temps': temps,
        'segment': 'temp_data',
    }
    return HttpResponse(html_template.render(context, request))
