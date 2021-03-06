from django import forms
from . import models


class addProfilepic(forms.ModelForm):
    class Meta:
        model = models.Profilepic
        fields = {'picture'}

    def __init__(self, *args, **kwargs):
        super(addProfilepic, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'