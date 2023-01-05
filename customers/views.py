from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer

#this will get all customers and details
def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customer': serializer.data})

#this will get individual customer details per id
def customer(request, id):
    data = Customer.objects.get(pk=id)
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})