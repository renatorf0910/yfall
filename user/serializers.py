from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'cpf', 'address', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Senha deve ser escrita apenas, não visível ao ler
        }
