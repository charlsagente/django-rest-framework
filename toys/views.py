from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from toys.models import Toy
from toys.serializers import ToysSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def toy_list(request):
    """
    Renders more than one toy
    """
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToysSerializer(toys, many=True)
        return Response(toys_serializer.data)

    elif request.method == 'POST':
        toys_serializer = ToysSerializer(data=request.data)
        if toys_serializer.is_valid():
            toys_serializer.save()
            return Response(toys_serializer.data, status=status.HTTP_201_CREATED)
        return Response(toys_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toys_serializer = ToysSerializer(toy)
        return Response(toys_serializer.data)

    elif request.method == 'PUT':
        toys_serializer = ToysSerializer(toy, data=request.data)
        if toys_serializer.is_valid():
            toys_serializer.save()
            return Response(toys_serializer.data)
        return Response(toys_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
