from APICreditScore import calculate
from django.shortcuts import render
from rest_framework.views import APIView
from APICreditScore.serializer import CreditScoreSerializer
from django.http import JsonResponse

# Create your views here.

class apiCreditScore(APIView):
    def get(self,request, *args, **kwargs):
        serializer = CreditScoreSerializer(data = request.GET)
        # http://127.0.0.1:8080/api/?simah=850&dbr=19&age=12-11-1961&income=850&marital_status=single&employer_type=government
        # http://127.0.0.1:8080/api/?simah=300&dbr=19&age=12-11-2002&income=1000&marital_status='married,divorced'&employer_type=student
        # http://127.0.0.1:8080/api/?simah=591&dbr=26&age=12-11-1960&income=5003&marital_status=single&employer_type='freelancer work'
        if serializer.is_valid():
            simah = serializer.validated_data ['simah']
            dbr   = serializer.validated_data['dbr']
            age = serializer.validated_data['age']
            income = serializer.validated_data['income']
            marital_status = serializer.validated_data['marital_status']
            employer_type = serializer.validated_data['employer_type']
            class_calculate = calculate.calculateCreditScore(simah=simah, dbr=dbr, age=age, income=income, marital_status=marital_status, employer_type=employer_type)
            percentage = class_calculate.getPercentage()
            return JsonResponse(percentage,status=201,safe=False)
        else:
            return JsonResponse(serializer.errors,status=400)

