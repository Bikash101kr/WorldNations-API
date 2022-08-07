from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from nations.models import Nations
from nations.serializers import NationSerializers
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def nations_list(request):
    if request.method == 'GET':
        nations = Nations.objects.all()


        name = request.GET.get('name', None)
        if name is not None:
            nations = nations.filter(name_icontains=name)

        nations_serializer = NationSerializers(nations, many=True)
        return JsonResponse(nations_serializer.data, safe=False)
#safe-fasle is for object serialization


    elif request.method == 'POST':
        nations_data = JSONParser().parse(request)
        nations_serializer = NationSerializers(data=nations_data)
        if nations_serializer.is_valid():
            nations_serializer.save()
            return JsonResponse(nations_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(nations_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def nations_detail(request, pk):
    try:
        nations = Nations.objects.get(pk=pk)
    except Nations.DoesNotExist:
        return JsonResponse({'message': 'The nation does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        nations_serializer = NationSerializers(nations)
        return JsonResponse(nations_serializer.data)

    elif request.method == 'GET':
        nations_data = JSONParser().parse(request)
        nations_serializer = NationSerializers(nations, data=nations_data)
        if nations_serializer.is_valid():
            nations_serializer.save()
            return JsonResponse(nations_serializer.data)
        return JsonResponse(nations_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        nations.delete()
        return JsonResponse({'message': 'Nation was deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)