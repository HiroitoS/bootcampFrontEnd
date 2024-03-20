
from rest_framework import serializers
from .models import *


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente

        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:

        model = Estudiante
        
        fields = '__all__'
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso

        fields = '__all__'

class CursoEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoEstudiante
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion

        fields = '__all__'


class PromedioCalificacionCursos(serializers.ModelSerializer):
    cursoId = CursoSerializer()

    class Meta:                         
        model= Calificacion
        fields = '__all__'


                
