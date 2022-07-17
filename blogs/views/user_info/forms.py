from blogs.models.blogs_user.blogs_user import Blogs_user

from django import forms


class BlogsUserForm(forms.ModelForm):
    class Meta:
        model = Blogs_user
        fields = ('photo', 'open_name','about',)