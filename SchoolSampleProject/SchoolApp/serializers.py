from rest_framework import serializers
from SchoolApp.models import Schools, Students

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schools
        fields=('school_id', 'school_name', 'max_student')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('school', 'student_id', 'name_first', 'name_last')