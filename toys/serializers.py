from rest_framework import serializers
from toys.models import Toy


class ToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = "__all__"


