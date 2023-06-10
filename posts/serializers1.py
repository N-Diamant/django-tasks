from rest_framework import serializers

#serializers are used to turn objects to json format

class PostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=504)
    contetnte  = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)
