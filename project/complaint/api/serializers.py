from rest_framework import serializers
from complaint.models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ['user_id']

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        return Complaint.objects.create(user_id=user, **validated_data)

