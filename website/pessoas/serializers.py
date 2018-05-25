from rest_framework import serializers
from pessoas.models import Pessoa, GENDERS

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'name', 'gender', 'age')