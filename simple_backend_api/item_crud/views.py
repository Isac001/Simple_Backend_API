# Django and Python Imports
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, response


# Local Imports
from .models import Item
from .serializers import ItemSerializer
from .logic import services, selectors


class ItemListView(generics.ListAPIView):

    serializer_class = ItemSerializer
    queryset = selectors.item_list()

class ItemDetailView(generics.RetrieveAPIView):

    serializer_class = ItemSerializer
    queryset = selectors.item_list()
    lookup_field = 'pk'

class ItemCreateView(generics.CreateAPIView):

    serializer_class = ItemSerializer
    queryset = selectors.item_list()

class ItemUpdateView(generics.UpdateAPIView):

    serializer_class = ItemSerializer
    queryset = selectors.item_list()
    lookup_field = 'pk'

class ItemDeleteView(generics.DestroyAPIView):

    queryset = selectors.item_list()
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        
        pk = self.kwargs.get('pk')

        try:

            selectors.item_delete(pk=pk)
            
            return response.Response(
                data={'Status': 'Item deletado com sucesso.'},
                status=status.HTTP_204_NO_CONTENT
            )

        except Item.DoesNotExist:    

            return response.Response(
                data={'errors': 'Item não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:

            return response.Response(
                data={'errors': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )