from rest_framework import generics
# from django.shortcuts import render
# from .models import Women
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .serializers import WomenSerializer
#
#
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import *
from rest_framework import viewsets

from women.models import Women, Category
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class WomenAPIList(generics.ListCreateAPIView): # три эти класса могут быть заменены одним WomenViewSet
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class WomenAPIDestroy(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class WomenViewSet(viewsets.ModelViewSet): # Работа с ViewSet
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_viewset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)

    # @action(methods=['get'], detail=False) # При detail=False можем получать только список категорий
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})

    # @action(methods=['get'], detail=True) # detail=True можем получать инфу по отдельным категориям
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})

# class WomenAPIList(generics.ListCreateAPIView): # Заменяем три эти класса одним WomenViewSet
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data) # Создание исключения для перехвата ошибки
#         serializer.is_valid(raise_exception=True)       # введения не полных данных
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, reguest, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = WomenSerializer(data=reguest.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         instance.delete()
#         return Response({"post": "delete post" + str(pk)})


