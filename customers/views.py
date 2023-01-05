from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer

#this will get all customers and details
def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customer': serializer.data})

#this will get individual customer details per id
def customer(request, id):
    #data = Customer.objects.get(pk=id)
    #adding exception to throw 404
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist: #specific exception
        raise Http404('Customer does not exist.')
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})