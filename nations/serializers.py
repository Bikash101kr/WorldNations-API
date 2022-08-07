from rest_framework import serializers
from nations.models import Nations


class NationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Nations
        fields = ('id','name','capital')