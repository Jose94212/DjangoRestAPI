from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    email=serializers.EmailField()
    id=serializers.IntegerField()


