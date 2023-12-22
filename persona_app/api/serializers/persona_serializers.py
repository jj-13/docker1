from rest_framework import serializers
from persona_app.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'nombre': instance.nombre,
            'apellidos': instance.apellidos,
            'tipo_documento': instance.tipo_documento,
            'documento': instance.documento,
            'hobbie': instance.hobbie
        }