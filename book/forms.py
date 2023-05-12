from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    #DA ESTILO AL FORM
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for f in iter(self.fields):
            self.fields[f].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Book
        fields= ('name', 'content')