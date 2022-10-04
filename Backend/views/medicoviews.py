from rest_framework import *
from rest_framework.response import Response
from Backend.serializers.userSerializer import UserSerializer

from rest_framework import APIView
from rest_framework import status
from rest_framework.response import Response


from Backend.models import medico
from Backend.serializers.medicoSerializer import MedicoSerializer


class medicoView(APIView):
    serializer_class = MedicoSerializer

    def get(self, request, *args,**kwargs):
        medicos = medico.objects.filter(id=kwargs['NunMedico'])
        medico_serializer = MedicoSerializer(medico,many=True)
        return Response(medico_serializer.data)

class medioCrear(APIView):

    serializer_class = MedicoSerializer

    def get(self, request, *args,**kwargs): 
        medicos=medico.objects.all()
        medico_serializer = MedicoSerializer(medico,many=True)
        return Response(medico_serializer.data)

    def post(self, request, *args, **kwargs):
        medico_serializer=MedicoSerializer(data=request.data)
        medico_serializer.is_valid(raise_exception=True)
        medico_serializer.save()
        return Response(medico_serializer.data,status=status.HTTP_201_CREATED)



