from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# this will get all customers and details


@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response({'customer': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this will get individual customer details per id
@api_view(['GET', 'POST', 'DELETE'])
def customer(request, id):
    # data = Customer.objects.get(pk=id)
    # adding exception to throw 404
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:  # specific exception
        # raise Http404('Customer does not exist.')
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serializer = CustomerSerializer(data)
        return Response({'customer': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)