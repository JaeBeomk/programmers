from django import forms

# 로그인시 입력받는Form
class LoginForm(forms.Form):
    username=forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder": "사용자명 (3자리이상)"}    
        ),
    )
    password=forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (4자리이상)"}    
        ),
    )
# 회원가입시 입력받는Form
class SignupForm(forms.Form):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    profile_image=forms.ImageField()
    short_description=forms.CharField()