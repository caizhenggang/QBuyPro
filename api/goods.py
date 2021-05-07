from rest_framework import serializers, viewsets

from goods.models import GoodsModel


# 序列化类
class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsModel
        fields = ('name', 'price', 'img1', 'info')


# API视图类
class GoodsAPIView(viewsets.ModelViewSet):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializer
