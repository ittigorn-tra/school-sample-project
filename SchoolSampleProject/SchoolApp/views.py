from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from SchoolApp.models import Schools, Students
from SchoolApp.serializers import SchoolSerializer, StudentSerializer


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

        return JsonResponse(data={'detail': 'Invalid request payload'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        school_data = JSONParser().parse(request)
        if 'school_id' not in school_data:
            return JsonResponse(data={'detail': '"school_id" is required in the payload'}, status=status.HTTP_400_BAD_REQUEST)
        existing_school = None
        try:
            existing_school = Schools.objects.get(school_id=school_data['school_id'])
        except Schools.DoesNotExist:
            return JsonResponse(data={'detail': 'School with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        schools_serializer = SchoolSerializer(existing_school, data=school_data)
        if schools_serializer.is_valid():
            schools_serializer.save()
            return JsonResponse(data={'detail': 'Updated successfully'}, safe=False)
        return JsonResponse(data={'detail': 'Failed to add'}, safe=False)

    elif request.method == 'DELETE':
        existing_school = None
        try:
            existing_school = Schools.objects.get(school_id=school_data['school_id'])
        except Schools.DoesNotExist:
            return JsonResponse(data={'detail': 'School with the given ID cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        existing_school.delete()
        return JsonResponse(data={'detail': 'Deleted successfully'}, safe=False)
