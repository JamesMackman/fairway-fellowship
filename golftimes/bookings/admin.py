from django.contrib import admin
from .models import GolfCourse, TeeTime, Booking

# Register your models here
@admin.register(GolfCourse)
class GolfCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(TeeTime)
class TeeTimeAdmin(admin.ModelAdmin):
    list_display = ('golf_course', 'datetime', 'availability')
    list_filter = ('golf_course', 'datetime')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('tee_time', 'user')
    list_filter = ('tee_time', 'user')
