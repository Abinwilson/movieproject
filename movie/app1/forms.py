from app1.models import Movie
from django import forms


class movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
