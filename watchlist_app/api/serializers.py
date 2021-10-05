from rest_framework import serializers
from watchlist_app.models import Watchlist,StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True , read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'




    # def get_len_name(self,objects):
    #     length = len(objects.name)
    #     return length

    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and description shouldn't be the same")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2 :
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value



# def name_len(value):
#         if len(value) < 2 :
#             raise serializers.ValidationError("name is too short")
#         else:
#             return value
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators=[name_len])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description shouldn't be the same")
#         else:
#             return data

#     # def validate_name(self, value):
#     #     if len(value) < 2 :
#     #         raise serializers.ValidationError("name is too short")
#     #     else:
#     #         return value

#     def create(self,validate_data):
#         return Movie.objects.create(**validate_data)
    
#     def update(self,instance,validate_data):
#         instance.name = validate_data.get('name',instance.name) 
#         instance.description = validate_data.get('description',instance.description) 
#         instance.active = validate_data.get('active',instance.active) 
#         instance.save()
#         return instance
    
