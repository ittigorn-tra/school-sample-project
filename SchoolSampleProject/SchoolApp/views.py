from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from SchoolApp.models import Schools, Students
from SchoolApp.serializers import SchoolSerializer, StudentSerializer


@csrf_exempt
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def schoolApi(request, id=None):

    if request.method == 'GET':
        if id is None:
            schools = Schools.objects.all()
            schools_serializer = SchoolSerializer(schools, many=True)
            return JsonResponse(schools_serializer.data, safe=False)
        else:
            school = None
            try:
                school = Schools.objects.get(school_id=id)
                schools_serializer = SchoolSerializer(school)
                return JsonResponse(schools_serializer.data, safe=False)
            except Schools.DoesNotExist:
                return JsonResponse(data={'detail': 'School with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        school_data = JSONParser().parse(request)
        schools_serializer = SchoolSerializer(data=school_data)
        if schools_serializer.is_valid():
            existing_school = None

            if school_data.get('school_id'):
                try:
                    existing_school = Schools.objects.get(school_id=school_data['school_id'])
                except Schools.DoesNotExist:
                    pass

            if not existing_school:
                schools_serializer.save()
                return JsonResponse(data={'detail': 'Added successfully'}, safe=False)
            else:
                return JsonResponse(data={'detail': 'School with the given ID already exists'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(data={'detail': schools_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        school_data = JSONParser().parse(request)
        if 'school_id' not in school_data:
            return JsonResponse(data={'detail': '"school_id" is required in the payload'}, status=status.HTTP_400_BAD_REQUEST)

        # check if school exceeds maximum capacity if updated
        if 'max_student' in school_data:
            school = Schools.objects.get(school_id=school_data['school_id'])
            students_in_this_school = Students.objects.filter(school_id=school_data['school_id']).count()
            if students_in_this_school > school_data['max_student']:
                return JsonResponse(data={'detail': 'Cannot adjust "max_student" to be lower than the existing student count'}, status=status.HTTP_409_CONFLICT)

        existing_school = None
        try:
            existing_school = Schools.objects.get(school_id=school_data['school_id'])
        except Schools.DoesNotExist:
            return JsonResponse(data={'detail': 'School with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        schools_serializer = SchoolSerializer(existing_school, data=school_data)
        if schools_serializer.is_valid():
            schools_serializer.save()
            return JsonResponse(data={'detail': 'Updated successfully'}, safe=False)
        return JsonResponse(data={'detail': schools_serializer.errors}, safe=False)

    elif request.method == 'DELETE':
        existing_school = None
        try:
            existing_school = Schools.objects.get(school_id=id)
        except Schools.DoesNotExist:
            return JsonResponse(data={'detail': 'School with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        existing_school.delete()
        return JsonResponse(data={'detail': 'Deleted successfully'}, safe=False)


@csrf_exempt
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def studentApi(request, id=None):

    if request.method == 'GET':
        if id is None:
            students = Students.objects.all()
            students_serializer = StudentSerializer(students, many=True)
            return JsonResponse(students_serializer.data, safe=False)
        else:
            student = None
            try:
                student = Students.objects.get(student_id=id)
                students_serializer = StudentSerializer(student)
                return JsonResponse(students_serializer.data, safe=False)
            except Students.DoesNotExist:
                return JsonResponse(data={'detail': 'Student with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        students_serializer = StudentSerializer(data=student_data)

        if students_serializer.is_valid():

            # check if school at maximum capacity
            school = Schools.objects.get(school_id=student_data['school_id'])
            students_in_this_school = Students.objects.filter(school_id=student_data['school_id']).count()
            if (students_in_this_school + 1) > school.max_student:
                return JsonResponse(data={'detail': 'This school is at its maximum capacity'}, status=status.HTTP_409_CONFLICT)

            students_serializer.save()
            return JsonResponse(data={'detail': 'Added successfully'}, safe=False)

        return JsonResponse(data={'detail': students_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        student_data = JSONParser().parse(request)
        if 'student_id' not in student_data:
            return JsonResponse(data={'detail': '"student_id" is required in the payload'}, status=status.HTTP_400_BAD_REQUEST)

        # check if school at maximum capacity
        if 'school_id' in student_data:
            school = Schools.objects.get(school_id=student_data['school_id'])
            students_in_this_school = Students.objects.filter(school_id=student_data['school_id']).count()
            if (students_in_this_school + 1) > school.max_student:
                return JsonResponse(data={'detail': 'This school is at its maximum capacity'}, status=status.HTTP_409_CONFLICT)

        existing_student = None
        try:
            existing_student = Students.objects.get(student_id=student_data['student_id'])
        except Students.DoesNotExist:
            return JsonResponse(data={'detail': 'Student with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        students_serializer = StudentSerializer(existing_student, data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse(data={'detail': 'Updated successfully'}, safe=False)
        return JsonResponse(data={'detail': students_serializer.errors}, safe=False)

    elif request.method == 'DELETE':
        existing_student = None
        try:
            existing_student = Students.objects.get(student_id=id)
        except Students.DoesNotExist:
            return JsonResponse(data={'detail': 'Student with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        existing_student.delete()
        return JsonResponse(data={'detail': 'Deleted successfully'}, safe=False)


@csrf_exempt
@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def schoolStudentsApi(request, id=None):
    students = Students.objects.filter(school_id=id).all()
    students_serializer = StudentSerializer(students, many=True)
    return JsonResponse(students_serializer.data, safe=False)
