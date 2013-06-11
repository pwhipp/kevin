from django import forms

class ActorSearchForm(forms.Form):
    last_name = forms.CharField(max_length=100,
                                label="Last name:")
    first_name = forms.CharField(max_length=100,
                                 label="First name:")
