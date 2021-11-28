from django.db.models import fields
from django.forms import forms
from usefulModels.models import Post

class PostForm(ModelForm):
    class Meta :
        model = Post
        fields = ['name_read', 'note']




