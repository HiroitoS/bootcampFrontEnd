from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import*
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from os import remove
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi




class DocenteRegistro(APIView):
    def get(self, request):
        respuesta = Docente.objects.all()
        serializador = DocenteSerializer(instance=respuesta, many=True)
        return Response(data={
            'message':'Informacion del Docente',
            'content': serializador.data
        })

    @swagger_auto_schema(
        request_body=DocenteSerializer,  
        responses={200: "Respuesta exitosa", 400: "Solicitud incorrecta"}  
    )
    def post(self, request):
        print(request.data)
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        serializador = DocenteSerializer(data=request.data)
        validacion = serializador.is_valid()
        if validacion:
            serializador.save()
            return Response(data={
                'message':'Docente Creado Exitosamente',
                'content': serializador.data
                
            })
        else:
            return Response(data={
                'message':'Error al crear al Docente',
                'content':serializador.errors
            })
        
class DocenteControler(APIView):
    def get(self, request, id):

        docente_encontrado = Docente.objects.filter(id=id).first()
        if not docente_encontrado:
            return Response(data={
                'message':'El docente no existe',
            })
        else:
            serializador = DocenteSerializer(instance=docente_encontrado)
            return Response(data={
                'message':'Docente encontrado',
                'content': serializador.data
            })
    @swagger_auto_schema(
        request_body=EstudianteSerializer,  
        responses={200: "Actualización exitosa", 400: "Solicitud incorrecta", 404: "No encontrado"}
    )
    def put(self, request, id):
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        docente_encontrado = Docente.objects.filter(id=id).first()
        if not docente_encontrado:
            return Response(data={
                'message':'El docente no existe',
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_anterior= docente_encontrado.foto.path

        serializador= DocenteSerializer(data=request.data)

        if serializador.is_valid():
            serializador.update(instance=docente_encontrado, 
                                validated_data=serializador.validated_data)
            
            remove(imagen_anterior)
            return Response(data ={
                'message': 'Docente actualizado exitosamente',
                'content': serializador.data
            })
        else:
            return Response(data={
                'message': 'Error al actualizar al Docente',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        docente_encontrado = Docente.objects.filter(id=id).first()
        if not docente_encontrado:
            return Response(data={
                'message': 'El docente no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_anterior= docente_encontrado.foto.path        
        Docente.objects.filter(id=id).delete()
        remove(imagen_anterior)
        return Response(data={
            'message':'El docente se elimino exitosamente'
        }, status=status.HTTP_204_NO_CONTENT)

class CrearCurso(APIView):
    @swagger_auto_schema(
        request_body=CursoSerializer,  
        responses={200: "Respuesta exitosa", 400: "Solicitud incorrecta"}  
    )
    def post(self, request):

        serializador = CursoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({
                'message': 'Curso agregado Exitosamente',
                'content': serializador.data

            }, status=status.HTTP_201_CREATED)  
        else:
            return Response({
                'message':'Error al guardar el curso',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        listar_cursos = Curso.objects.all()
        if not listar_cursos:
            return Response({
                'message':'Los cursos no existen'
            })
        else:
            serializador = CursoSerializer(instance=listar_cursos, many=True)
            return Response({
                'content': serializador.data
            })

class ListarCalificaciones(APIView):
    def get (self,request):
        calificacion_curso = Calificacion.objects.all()
        
        serializador = PromedioCalificacionCursos(instance=calificacion_curso, many=True)
        return Response(data={
                'content':serializador.data
            })
    
    
class CalificarCursos(APIView):
    @swagger_auto_schema(
        request_body=CalificacionSerializer,  
        responses={200: "Respuesta exitosa", 400: "Solicitud incorrecta"}  
    )
    def post(self,request,id):
        serializador = CalificacionSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({
                'message':'calificaciones agregadas exitosamente',
                'content':serializador.data
            })
        else:
            return Response({
                'message':'Error al guardar calificaciones',
                'content':serializador.errors
            })

class EstudianteRegistro(APIView):
    @swagger_auto_schema(
        request_body=EstudianteSerializer,  
        responses={200: "Respuesta exitosa", 400: "Solicitud incorrecta"}  
    )   
    def post(sefl, request):
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        serializador = EstudianteSerializer(data=request.data)
        validacion=serializador.is_valid()
        
        if validacion:
            serializador.save()
            return Response(data={
                'message':'Estudiante creado exitosamente',
                'content': serializador.data
            })
        else:
            return Response(data={
                'message':'Error al crear estudiante',
                'content':serializador.errors
            })
        
    def get(self, request):
        estudiante_encontrado = Estudiante.objects.all()
        serializador = EstudianteSerializer(instance=estudiante_encontrado, many=True)
        if estudiante_encontrado:
            return Response(data={
                'mensage':'el estudiante si existe',
                'content': serializador.data
            })

class EstudianteControler(APIView):
    def get(self,request,id):
        estudiante_encontrado=Estudiante.objects.filter(id=id).first()
        if not estudiante_encontrado:
            return Response(data={
            'message':'El estudiante no existe'
            })
        else:
            serializador = EstudianteSerializer(instance=estudiante_encontrado)
            return Response(data={
                'message':'estudiante encontrado',
                'content': serializador.data
            })
        
    @swagger_auto_schema(
        request_body=EstudianteSerializer,  
        responses={200: "Actualización exitosa", 400: "Solicitud incorrecta", 404: "No encontrado"}
    )    
    def put(self, request, id):
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        alumno_encontrado = Estudiante.objects.filter(id=id).first()
        if not alumno_encontrado:
            return Response(data={
                'message':'El estudiante no existe',
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_anterior= alumno_encontrado.foto.path

        serializador= EstudianteSerializer(data=request.data)

        if serializador.is_valid():
            serializador.update(instance=alumno_encontrado, 
                                validated_data=serializador.validated_data)
            
            remove(imagen_anterior)
            return Response(data ={
                'message': 'El estudiante se actualizo exitosamente',
                'content': serializador.data
            })
        else:
            return Response(data={
                'message': 'Error al actualizar el Estudiante',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)    