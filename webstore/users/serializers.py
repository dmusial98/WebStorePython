from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'email', 'is_staff', 'active', 'phone',  'address') # if not declared, all fields of the model will be shown