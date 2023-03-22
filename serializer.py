from rest_framework import serializers
from social.models import Messages

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model= Messages
		fields = '__all__'



