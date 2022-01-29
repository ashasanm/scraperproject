from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Product
from .serializers import ProductSerializer
from tools.amazon import Amazon
from tools.ebay import Ebay

amazon = Amazon()
ebay = Ebay()

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def scrapProducts(request):
    json_data = request.data
    if "amazon" in json_data["url"]:
        product = amazon.scrap_product(json_data["url"])

        return Response(product)

    elif "ebay" in json_data["url"]:
        product = ebay.scrap_product(json_data["url"])

        return Response(product)
        
    else:
        msg = {
            "message": "Unsupported web"
        }
        return Response(msg, status=status.HTTP_404_NOT_FOUND)