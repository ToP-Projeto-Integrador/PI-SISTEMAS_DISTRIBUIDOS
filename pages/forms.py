from django import forms
from .models import UploadFile, Produto

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = "__all__"


class FormCProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
