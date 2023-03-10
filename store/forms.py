from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput
from .models import Contact, Booking
from django.forms.utils import ErrorList

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=["name", "email",]
        widget={
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])

    
    