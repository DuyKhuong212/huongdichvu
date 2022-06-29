from rest_framework import serializers
from .models import Award, FormApply, StudentTranscript, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'first_name', 'last_name', 'username', 'password', 'email', 'date_joined', 'is_superuser','name',"masv",'adress')
        extra_kwargs = {
            'password': {'write_only': 'true'},
            'email': {'required': 'true'}
        }

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

            is_superuser=validated_data['is_superuser']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'desc', 'price')



class StudentTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTranscript
        fields = ('student_id','name', 'poin')

    def to_representation(self, instance):
        rep = super(StudentTranscriptSerializer, self).to_representation(instance)
        rep['name'] = instance.student_id.username
        return rep



class FormApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormApply
        fields = ('id','student_id', 'award_id', 'context', 'email','status','point')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['student_id']=UserSerializer(instance.student_id).data
        rep['award_id']=AwardSerializer(instance.award_id).data
        return rep

