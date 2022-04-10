from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import DoctorVisitsForm
from .forms import FamilyVisitsForm
from .forms import MedicineForm

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

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

#
# @login_required(login_url="/login/")
# def pages(request):
#     print(request)
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
#
#         load_template = request.path.split('/')[-1]
#         print(request.method, load_template)
#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         if load_template == 'doctors':
#             if request.method == "POST":
#                 form = DoctorVisitsForm(request.POST, request.FILES)
#                 print(form)
#                 if form.is_valid():
#                     venue = form.save(commit=False)
#                     venue.owner = request.user.id  # logged in user
#                     venue.save()
#                     # form.save()
#                     return HttpResponseRedirect(reverse('doctors:index'))
#                 else:
#                     form = DoctorVisitsForm
#                     if 'submitted' in request.GET:
#                         # submitted = True
#                         html_template = loader.get_template(
#                             'home/' + load_template)
#                     return HttpResponse(html_template.render(context, request))
#             else:
#                 print('loaded')
#                 return HttpResponseRedirect(reverse('doctors:index'))
#
#         context['segment'] = load_template
#
#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))
#
#     except template.TemplateDoesNotExist:
#
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))
#
#
# def medicines(request):
#     path = HttpRequest.path()
#     print('@@@@', path)
#     return render(request, 'home/medicines.html')

# @login_required(login_url="/login/")


def doctor_visits(request):
    form = DoctorVisitsForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    submitted = False
    if request.method == "POST":
        if form.is_valid():
            venue = form.save()
            venue.owner = request.user.id  # logged in user
            venue.save()
            print(venue)
            submitted = True
            # form.save()
        else:
            form = DoctorVisitsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
    }
    return HttpResponse(html_template.render(context, request))

def family_visits(request):
    form = FamilyVisitsForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.owner = request.user.id  # logged in user
            venue.save()
            submitted = True
            # form.save()
        else:
            form = FamilyVisitsForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
    }
    return HttpResponse(html_template.render(context, request))

def medicine(request):
    form = MedicineForm(request.POST)
    load_template = request.path.split('/')[-1] + '.html'
    submitted = False
    if request.method == "POST":
        print(request.method, form.errors)
        if form.is_valid():
            venue = form.save()
            venue.owner = request.user.id  # logged in user
            venue.save()
            submitted = True
            # form.save()
        else:
            form = MedicineForm
    html_template = loader.get_template('home/' + load_template)
    context = {
        'form': form,
        'success': submitted,
    }
    return HttpResponse(html_template.render(context, request))