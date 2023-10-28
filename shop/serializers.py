from rest_framework import serializers


class DelayReportSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=16)
    order_id = serializers.IntegerField()


