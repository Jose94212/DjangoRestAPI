from rest_framework import serializers 
from app_tutorial.models import AppTutorials
 
 
class AppTutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AppTutorials
        fields = ('id',
                  'title',
                  'description', 'published'
        )
    