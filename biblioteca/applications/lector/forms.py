from django import forms
from django.forms import widgets

from applications.libro.models import Libro

from .models import Prestamo

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = [
            'lector',
            'libro',
        ]
class MultiPrestamoForm(forms.ModelForm):

    libros = forms.ModelMultipleChoiceField(
        queryset = None,
        required = True,
        widget = forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Prestamo
        fields = [
            'lector',
        ]

        widgets = {
            'lector': forms.Select(
                attrs={'class':'form-control mb-2 w-25'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(MultiPrestamoForm, self).__init__(*args, **kwargs)

        self.fields['libros'].queryset = Libro.objects.all()
    