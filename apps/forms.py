from django import forms
from apps.models import Notifica

class NotificaForm (forms.ModelForm):
    class Meta:
        model = Notifica
        fields = [
            'email',
        ]