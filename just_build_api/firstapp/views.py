from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Reservation

# function based view
def hello_world(request):
    reservations: QuerySet = Reservation.objects.all().values()

    return JsonResponse(list(reservations), safe=False)



# class based view
class HelloTest(View):
    def get(self, request):
        return HttpResponse("Hello Test")

