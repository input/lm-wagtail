from wagtail.users.forms import UserCreationForm, UserEditForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")


class CustomUserEditForm(UserEditForm):

    class Meta(UserEditForm.Meta):
        model = CustomUser
        fields = ("username", "email")
