# coding: utf-8
from rest_framework import serializers
from .models import CarouselImg,BulletIn

class CarouselImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImg
        fields = ('name','image')

class BulletInSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletIn
        fields = ('name','bulletin')
    
