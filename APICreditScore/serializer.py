from rest_framework import serializers

from typing import AsyncGenerator


class CreditScoreSerializer(serializers.Serializer):
    DATE_INPUT_FORMATS = ['%d-%m-%Y']
    simah = serializers.IntegerField(required=True)
    dbr   = serializers.IntegerField(required=True)
    age = serializers.DateField(input_formats=DATE_INPUT_FORMATS, required=True)
    income = serializers.IntegerField(required=True)
    marital_status = serializers.CharField(max_length=18, required=True)
    employer_type = serializers.CharField(max_length=18, required=True)

    def __init__(self,*args, **kwargs):
        super(CreditScoreSerializer,self).__init__(*args, **kwargs)

    def validate(self,data):

        return data