from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TeeTime, Booking
from .forms import BookingForm

def golf_course_list(request):
    golf_courses = GolfCourse.objects.all()
    return render(request, 'bookings/golf_course_list.html', {'golf_courses': golf_courses})

def tee_time_list(request, golf_course_id):
    golf_course = GolfCourse.objects.get(pk=golf_course_id)
    tee_times = TeeTime.objects.filter(golf_course=golf_course)
    return render(request, 'bookings/tee_time_list.html', {'golf_course': golf_course, 'tee_times': tee_times})

def book_tee_time(request, tee_time_id):
    tee_time = TeeTime.objects.get(pk=tee_time_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user  # Assuming user is logged in
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
