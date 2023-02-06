#아이디 못바꾸게 하기 위해
from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #이 문장이 들어오면서 초기화 이후에 username 칸을 비활성화 시켜서 못 바꾸게 만든다.
        self.fields['username'].disabled = True
