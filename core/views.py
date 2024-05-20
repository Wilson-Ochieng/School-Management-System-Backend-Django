from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher, Exam, Grade, Account
from .serializers import StudentSerializer, TeacherSerializer,ExamSerializer,GradeSerializer,AccountSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # Check if a student with the same admission_no already exists
        if Student.objects.filter(admission_no=data['admission_no']).exists():
            return Response({'error': 'A student with this admission number already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()  # Make a copy of the request data

        # Ensure admission_no is not changed
        data['admission_no'] = instance.admission_no

        serializer = self.get_serializer(instance, data=data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()  # Make a copy of the request data

        # Ensure admission_no is not changsed
        data['admission_no'] = instance.admission_no

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    



    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # Check if a student with the same admissi1on_no already exists
        if Teacher.objects.filter(tsc_no=data['tsc_no']).exists():
            return Response({'error': 'A Teacher with this TSC number already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        if 'tsc_no' in data and Teacher.objects.filter(tsc_no=data['tsc_no']).exclude(id=instance.id).exists():
            return Response({'error': 'A Teacher with this TSC number already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer