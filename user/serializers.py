from rest_framework import serializers
from django.contrib.auth.models import User, Group
from constants import APPLICANT_ROLE


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'groups')
        read_only_fields = ('id',)

    def create(self, validated_data):
        group_name = validated_data.pop('group', APPLICANT_ROLE)
        groups_data = validated_data.pop('groups', [])
        user = User.objects.create_user(**validated_data)
        if group_name:
            group_instance = Group.objects.filter(name=group_name).first()
            if group_instance:
                user.groups.add(group_instance)
        if groups_data:
            group_instances = Group.objects.filter(name__in=groups_data)
            user.groups.set(group_instances)
        return user


# Serializador para User
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Campos del usuario que quieres mostrar
