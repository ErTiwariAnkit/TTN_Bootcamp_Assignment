from django import forms
class studentreg(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    age=forms.IntegerField()