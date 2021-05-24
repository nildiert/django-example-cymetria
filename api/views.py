from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import OfficeInventorySerializer

from .models import OfficeInventory

# Create your views here.
class HelloView(APIView):

    serializer_class = OfficeInventorySerializer

    def get(self, request, *args, **kwargs):

        import pdb; pdb.set_trace()
        queryset = OfficeInventory.objects.all()
        serializer = OfficeInventorySerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = OfficeInventorySerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        new_name = kwargs.get('name')
        pk = kwargs.get('pk')

        office_inventory = OfficeInventory.objects.get(pk=pk)
        office_inventory.name = new_name
        office_inventory.save()
        
        return Response({'message': 'updated'})

    