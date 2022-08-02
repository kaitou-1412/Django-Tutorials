from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # custom field
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['name']

    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different!")
        return data

    def get_len_name(self, object):
        return len(object.name)
    
    # field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value

# # validator
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different!")
#         return data
#
#     # field level validation
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     return value
