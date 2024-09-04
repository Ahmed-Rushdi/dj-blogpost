from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "slug", "banner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "w-full p-2 text-darkest rounded"
