import json
from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Job, Booking
from .forms import JobForm, BookForm
from accounts.models import CustomUser


def job_list(request, job_type, city):
    #jobs = Job.objects.filter(job_type=job_type, provider__city=city).all()
    jobs = Job.objects.filter(job_type__icontains=job_type, provider__provider__city=city.lower()).all()
    return render(request, 'job_list.html', {'jobs': jobs, 'job_type': job_type})

def home_page(request):
    form = JobForm()
    sign_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'index.html', {'form': form, 'sign_form': sign_form, 'login_form': login_form, 'user': request.user})

def job_redirect(request):
    if request.method == 'POST':
        city = request.POST.get('city').split(", ")[0]
        job_type = request.POST.get('job_type')
        return redirect('job_list', job_type=job_type[2:-2], city=city)
    else:
        return HttpResponseNotAllowed(['POST'])

def job_type_complete(request):
    if request.is_ajax():
        job_type = request.GET.get('term', '')
        available_types = Job.objects.filter(job_type__icontains=job_type).all()[:5]
        results = []
        for job in available_types:
            print (job, flush=True)
            results.append(job.job_type)
        data = json.dumps(results)
        result_json = {'suggestions': data}
        print(result_json, flush=True)
    return JsonResponse(result_json)

def book_page(request, pk):
    if request.method == "POST":
        date_day = int(request.POST.get('date_day'))
        date_month = int(request.POST.get('date_month'))
        date_year = int(request.POST.get('date_year'))
        chosen_date = date(date_year, date_month, date_day)
        booked_job = Job.objects.get(pk=pk)
        new_book = Booking.objects.create(client=request.user, booked_job=booked_job, date=chosen_date)
        return redirect('bookings')
    else:
        form = BookForm()
        return render(request, 'book_page.html', {'form': form})

def bookings(request):
    bookings_list = Booking.objects.filter(client=request.user).all()
    return render(request, 'bookings.html', {"bookings": bookings_list})
# Create your views here.
