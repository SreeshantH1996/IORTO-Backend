from rest_framework import serializers

from registration.models import *


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


class OtherDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDocuments
        fields = "__all__"


class UserRenewalDataSerializer(serializers.ModelSerializer):
    dob = serializers.SerializerMethodField()
    licencefrom = serializers.SerializerMethodField()
    licenceto = serializers.SerializerMethodField()

    class Meta:
        model = LicenceRenewalApplication
        fields = "__all__"

    def get_dob(self, obj):
        return obj.dob.strftime("%Y-%m-%d")

    def get_licenceto(self, obj):
        return obj.licenceto.strftime("%Y-%m-%d")

    def get_licencefrom(self, obj):
        return obj.licencefrom.strftime("%Y-%m-%d")


class RtoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RtoOfficer
        fields = ["district", "officerid", "id"]


class UserSerializerforRTO(serializers.ModelSerializer):
    class Meta:
        model = StandUser
        fields = ["district", "name", "id", "phnumber", "user_status", "renewal_status"]


class LicenceRenewalSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    renewal_status = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    dob = serializers.SerializerMethodField()
    licencefrom = serializers.SerializerMethodField()
    licenceto = serializers.SerializerMethodField()

    class Meta:
        model = LicenceRenewalApplication
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.name

    def get_renewal_status(self, obj):
        return obj.user.renewal_status

    def get_dob(self, obj):
        return obj.dob.strftime("%Y-%m-%d")

    def get_licenceto(self, obj):
        return obj.licenceto.strftime("%Y-%m-%d")

    def get_licencefrom(self, obj):
        return obj.licencefrom.strftime("%Y-%m-%d")

    def get_status(self, obj):
        return obj.user.user_status


class LicenceApplicationSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    dob = serializers.SerializerMethodField()

    class Meta:
        model = LicenceApplication
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.name

    def get_dob(self, obj):
        return obj.dob.strftime("%Y-%m-%d")

    def get_status(self, obj):
        return obj.user.user_status
