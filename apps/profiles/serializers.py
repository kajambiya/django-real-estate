from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    firstname = serializers.CharField(source="user.firstname")
    lastname = serializers.CharField(source="user.lastname")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "username",
            "firstname",
            "lastname",
            "full_name",
            "email",
            "id",
            "phone_number",
            "profile_photo",
            "about_me",
            "license",
            "gender",
            "country",
            "city",
            "is_buyer",
            "is_seller",
            "is_agent",
            "rating",
            "num_reviews",
            "reviews",
        ]

    def get_full_name(self, obj):
        firstname = obj.user.firstname.title()
        lastname = obj.user.lastname.title()
        return f'{firstname} {lastname}'

    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'profile_photo',
            'about_me',
            'license',
            'gender',
            'country',
            'city',
            'is_buyer',
            'is_seller',
            'is_agent',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation
