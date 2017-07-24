from rest_framework import serializers
from api.models.Room import Room
from api.models.Judge import Judge
from api.models.Team import Team
from api.models.SortedRoom import SortedRoom
from api.models.VPIPreference import VPIPreference
from api.models.Member import Member
from api.models.SignUpPreference import SignUpPreference

class RoomSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Room
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = ('id', 'member_id', 'sorted_room_id' 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = ('id', 'debater_one_id', 'debater_two_id', 'skill_level', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class SortedRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedRoom
        fields = ('id', 'og_id', 'oo_id', 'cg_id', 'co_id', 'room_id', 'skill_level', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class SignUpPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedRoom
        fields = ('id', 'member_id', 'name', 'partner_preference', 'debate_preference', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class VPIPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedRoom
        fields = ('id', 'judgeless_rooms', 'room_type', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

# TODO double check if fields from Django user default model should be listed
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedRoom
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'skill_level', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
