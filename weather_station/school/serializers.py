from .models import School
from rest_framework import serializers

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('name','eng_name','school_abbreviation')
