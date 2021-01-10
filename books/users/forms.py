from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# User = get_user_model()
# users = User.objects.all()
# print(users)


class CustomUserCreationForm(UserCreationForm):

    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomerUserChangeForm(UserChangeForm):


    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)