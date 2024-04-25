from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import GolfCourse, TeeTime, Booking
from .forms import BookingForm

class GolfCourseListView(ListView):
    model = GolfCourse
    template_name = 'bookings/golf_course_list.html'
    context_object_name = 'golf_courses'

class TeeTimeDetailView(DetailView):
    model = TeeTime
    template_name = 'bookings/tee_time_detail.html'
    context_object_name = 'tee_time'

@login_required
def book_tee_time(request, tee_time_id):
    tee_time = get_object_or_404(TeeTime, pk=tee_time_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user
            booking = form.save(commit=False)
            booking.tee_time = tee_time
            booking.user = user
            booking.save()
            tee_time.availability -= 1
            tee_time.save()
            messages.success(request, 'Tee time booked successfully!')
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'tee_time': tee_time, 'form': form})


