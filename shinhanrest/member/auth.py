from django.contrib.auth.hashers import check_password
from .models import Member

class MemberAuth: # 상속받지 않고 class에 2개의 함수를 만듬

    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        # 장고 모델을 상속 받았기 때문에 username과 password를 쓸 수 있다
        # username , password에 기본값을 넣은 이유는 인증 백엔드에서 username과 password를 사용하는 것을 알기 때문에 
        # 장고가 기본으로 제공하는 username으로 꼭 로그인하는 경우는 없다.. 이메일로 로그인할 수도 있음
        # 만약 def authenticate(self, request, *args, **kwargs)로 쓰면 username = kwargs.get('username) 으로 아래 써도 됨
        if not username or not password: # 아이디가 없거나 비밀번호가 없다면 none인데
            if request.user.is_authenticated:  # 이미 로그인 되어 있으면 user을 return 
                return request.user
            return None # 생략하면 그냥 None

        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None
        
        if check_password(password, member.password): # 비밀번호 확인
            if member.status == '일반': # 일반 인지 확인
                return member
        return None
    
    def get_user(self, pk): # pk가 전달되고, Member을 가지고 와서 반환
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist: # 못찾으면 none 값 반환 (none을 안쓰고 return 만 해도 none값 반환 의미)
            return None
        return member # if member.is_active and member.status == '일반' else None 에 대한 처리를 인증 단계에서 함 (안써도 됨)