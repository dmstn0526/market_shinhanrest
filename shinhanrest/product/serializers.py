from rest_framework import serializers
# from rest_framework.exceptions import ValidationError


from .models import Product, Comment, Like

class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    # 필드가 추가되었는데, 생성할때도 serializer를 거쳐가지만
    # method 필드이기 때문에 반환을 위한 method라 인지하기 때문에
    # 값을 setting해서 넘기지 않아도 됨
    likt_count = serializers.SerializerMethodField()
    
    def get_comment_count(self,obj): # get_field명
        # obj = serializer로 전달된 객체를 의미
        # database에는 aggregation
        return obj.comment_set.all().count() # 모델명(소문자)_set = 1:n 관계에서 n의 정보를 가져 올때 set으로 가져옴

        # return Comment.objects.filter(product=obj).count()
        # aggregation count = count를 호출해서 개수만 반환
    
    def get_like_count(self,obj):
        return obj.comment_set.all().count()

    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer): # 가져가기 위한 serializer
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer): # 생성을 위한 serializer
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required = False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {'member':{'required':False}}

class LikeCreateSerializer(serializers.ModelSerializer): # 생성을 위한 serializer
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required = False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model = Like
        fields = '__all__'
        # extra_kwargs = {'member':{'required':False}}