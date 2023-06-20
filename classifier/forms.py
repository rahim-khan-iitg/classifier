from django import forms
class Image(forms.Form):
    image=forms.ImageField(allow_empty_file=False,required=True)