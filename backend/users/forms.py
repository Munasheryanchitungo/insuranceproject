from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    mobile = forms.CharField(max_length=20, required=True)
    business_type = forms.ChoiceField(
        choices=[
            ('grocery', 'Grocery'),
            ('clothing', 'Clothing'),
            ('agriculture', 'Agriculture'),
            ('other', 'Other'),
        ],
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'business_type', 'password1', 'password2']