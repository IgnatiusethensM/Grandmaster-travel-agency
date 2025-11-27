from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from bookings.models import Booking

@login_required
def dashboard(request):
    today = timezone.now().date()
    bookings = Booking.objects.filter(user=request.user).order_by('check_in_date')
    
    upcoming_bookings = bookings.filter(check_in_date__gte=today)
    past_bookings = bookings.filter(check_in_date__lt=today)
    
    context = {
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
    }
    return render(request, 'dashboard/index.html', context)
