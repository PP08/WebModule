from django import forms
from .models import Document_Single, Document_Multiple

class DocumentForm_Single(forms.ModelForm):
    class Meta:
        model = Document_Single
        fields = ('single', )

class DocumentForm_Multiple(forms.ModelForm):
    class Meta:
        model = Document_Multiple
        fields = ('multiple',)