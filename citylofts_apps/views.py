

from django.shortcuts import render, redirect
from .models import LoftRentals, TemporaryStandRental, CoMinimizing, LoftFeature

# Create your views here.


def index(request):
    return render(request, 'citylofts_apps/index.html')






def lofts_rental_view(request):
    if request.method == 'POST':
        # Process and save data from the LoftRentals form
        # Remember to validate and clean the data before saving
        # You can use forms or manual validation to handle the data

        # For example:
        rent_value_euro = request.POST.get('rent_value_euro')
        present_status = request.POST.get('present_status')
        rental_period_from = request.POST.get('rental_period_from')
        rental_period_to = request.POST.get('rental_period_to')
        loft_number = request.POST.get('loft_number')

        # Save the data to the database using the LoftRentals model
        # For example:
        LoftRentals.objects.create(rent_value_euro=rent_value_euro, present_status=present_status,
                                   rental_period_from=rental_period_from, rental_period_to=rental_period_to,
                                   loft_number=loft_number)

        return redirect('citylofts_apps:index')


    return render(request, 'citylofts_apps/lofts-rental.html')  # Redirect to the same page after submitting the form

    

def temporary_stand_rental_view(request):
    if request.method == 'POST':
        # Process and save data from the TemporaryStandRental form
        # Remember to validate and clean the data before saving
        # You can use forms or manual validation to handle the data

        # For example:
        rent_day_value_yi = request.POST.get('rent_day_value_yi')
        present_status_yi = request.POST.get('present_status_yi')
        rental_period_from_yi = request.POST.get('rental_period_from_yi')
        rental_period_to_yi = request.POST.get('rental_period_to_yi')

        rent_day_value_yang = request.POST.get('rent_day_value_yang')
        present_status_yang = request.POST.get('present_status_yang')
        rental_period_from_yang = request.POST.get('rental_period_from_yang')
        rental_period_to_yang = request.POST.get('rental_period_to_yang')

        TemporaryStandRental.objects.create(
            rent_day_value_yi=rent_day_value_yi,
            present_status_yi=present_status_yi,
            rental_period_from_yi=rental_period_from_yi,
            rental_period_to_yi=rental_period_to_yi,
            rent_day_value_yang=rent_day_value_yang,
            present_status_yang=present_status_yang,
            rental_period_from_yang=rental_period_from_yang,
            rental_period_to_yang=rental_period_to_yang
        )

        return redirect('citylofts_apps:index')  # Redirect to the same page after submitting the form

    return render(request, 'citylofts_apps/temporary_stand_rental.html')  # Render the template for TemporaryStandRental form





def co_minimizing_view(request):
    co_minimizing_items = CoMinimizing.objects.all()
    print(co_minimizing_items)  # Check if any items are retrieved from the database
    return render(request, 'citylofts_apps/co_minimizing.html', {'co_minimizing_items': co_minimizing_items})
