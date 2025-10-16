from rest_framework import generics
from test_proj.main.apps.product.services import ProductService 
from .models import Product
from .serializer import ProductCreateSerializer, ProductSerializer, ProductUpdateSerializer
from ..common.pagination import CustomPagination
from .documents import ProductDocument
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from elasticsearch_dsl import Q, Search
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     pagination_class = CustomPagination
#     authentication_classes = [authentication.JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return ProductCreateSerializer
#         else:
#             return ProductSerializer




# class ProductSearch(APIView):
#     serializer_class = ProductSerializer
#     document_class = ProductDocument

#     def generate_q_expression(self, query):
#         return Q(
#             "multi_match",
#             query=query,
#             fields=["title"],
#             fuzziness="auto"
#         )

#     def get(self, request, query):
#         q = self.generate_q_expression(query)
#         search = self.document_class.search().query(q)
#         return Response(self.serializer_class(search.to_queryset(), many=True).data)


# product_search_api_view = ProductSearch.as_view()


# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     authentication_classes = [authentication.JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field='guid'

#     def get_serializer_class(self):
#         if self.request.method == 'PUT' or 'PATCH':
#             return ProductUpdateSerializer
#         else:
#             return ProductSerializer

# product_retrieve_update_delete_api_view = ProductDetailView.as_view()




class ProductAPIView(APIView):
    def get(self, request):
        products = ProductService.list_product()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = ProductService.create_product(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

product_list_create_api_view = ProductAPIView.as_view()





class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = ProductService.retrieve_product(pk)
        if not product:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = ProductService.retrieve_product(pk)
        if not product:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            updated_product = ProductService.update_product(product, serializer.validated_data)
            return Response(ProductSerializer(updated_product).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = ProductService.retrieve_product(pk)
        if not product:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        ProductService.delete_product(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

product_retrieve_update_delete_api_view = ProductDetailAPIView.as_view()