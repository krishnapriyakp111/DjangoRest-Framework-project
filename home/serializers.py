from rest_framework import serializers
from .models import Person, Color


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']


class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_color_info(self, obj):
        color_obj = Color.objects.get(id=obj.color.id)
        return {'color_name': color_obj.color_name, 'hex_code': '#0005'}

    def validate(self, data):
        special_chars ='!@#$%^&*()?'
        if any(c in special_chars for c in data['name']):
            raise serializers.ValidationError('special character not allowed')
        if data['age'] < 18:
            raise serializers.ValidationError('age of the person should be grater than 18')
        return data