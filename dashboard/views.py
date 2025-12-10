from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
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

def is_staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_check)
def staff_dashboard(request):
    bookings = Booking.objects.all().order_by('-created_at')
    
    # Simple filtering
    status_filter = request.GET.get('status')
    if status_filter:
        bookings = bookings.filter(status=status_filter)

    # Calculate some stats
    total_revenue = sum(b.total_price for b in bookings if b.payment_status == 'PAID')
    pending_count = bookings.filter(status='PENDING').count()
    
    context = {
        'bookings': bookings,
        'total_revenue': total_revenue,
        'pending_count': pending_count,
    }
    return render(request, 'dashboard/staff_index.html', context)

@login_required
@user_passes_test(is_staff_check)
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        new_payment = request.POST.get('payment_status')
        
        if new_status:
            booking.status = new_status
        if new_payment:
            booking.payment_status = new_payment
            
        booking.save()
        messages.success(request, f'Booking #{booking.id} updated successfully.')
        
    return redirect('staff_dashboard')
