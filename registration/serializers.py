from rest_framework import serializers

from registration.models import LicenceApplication, UserDocuments


class ApplicationDetails(serializers.ModelSerializer):
    dob = serializers.SerializerMethodField()

    class Meta:
        model = LicenceApplication
        fields = "__all__"

    def get_dob(self, obj):
        return obj.dob.strftime("%Y-%m-%d")


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocuments
        fields = "__all__"
