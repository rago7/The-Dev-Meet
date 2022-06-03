from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class TagSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerilizer(serializers.ModelSerializer):
    owner = ProfileSerilizer()
    class Meta:
        model = Review
        fields = '__all__'

class ProjectSerilizer(serializers.ModelSerializer):
    owner = ProfileSerilizer(many=False) # many is the relation 
    tags = TagSerilizer(many=True)
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerilizer(reviews, many=True)
        return serializer.data