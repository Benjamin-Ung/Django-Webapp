from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

#view which shows all routes in api
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',

    ]
    #safe allows response to contain more than Python dictionary
    return Response(routes)

#returns all rooms available
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    
    #many parameter asks if there are multiple objects to be serialized
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    #many parameter asks if there are multiple objects to be serialized
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)