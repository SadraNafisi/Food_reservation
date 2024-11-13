from rest_framework.decorators import api_view
from rest_framework.response import Response
from reservation.models import Item , SubOrder
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from reservation.models import Order , SubOrder
from .serializer import *
@api_view(['GET'])
def getRoute(request):
    routes=[
        {'GET':'order-list-all/'},
        {'GET':'order-list/'},
    ]
    return Response(routes)
@api_view(['GET'])
def getItem(request):
    items = Item.objects.all()

    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)
@api_view(['GET'])
def getSuborder(request):
    suborders = SubOrder.objects.all()

    serializers = SuborderSerializer(suborders, many=True)
    return Response(serializers.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addSuborder(request):
    order,created = Order.objects.get_or_create(
        customer=request.user,
        is_confirmed=False
    )
    item = Item.objects.get(pk=request.data['itemPK'])
    if(item.available == False):
        return Response({"message":"this item is not available!"})
    amount = request.data['amount']
    if(order.suborder_set.filter(item = item)):
        return Response({"message": "this suborder already exists!"})
    suborder = SubOrder.objects.create(item=item, amount=amount, order= order)
    serializer = SuborderSerializer(suborder,many=False)
    print(request.data)
    return Response(serializer.data)
