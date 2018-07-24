from django import forms
import re
from django.core.exceptions import ValidationError
from ..models import Records


class AddForm(forms.ModelForm):
    class Meta:
        model = Records
        exclude = ('id',)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=120)

    def clean(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        if name and email:
            email_verify = re.compile(r'''[^@]+@[^@]+\.[^@]+''')
            print(email_verify.match(email))
            if email_verify.match(email):
                return self.cleaned_data
            else:
                raise ValidationError({'email': 'The email is invalid'})
            return self.cleaned_data
        else:
            raise ValidationError({"email": "Please check Your input"})
