from django import forms
from .models import Usuario, UsuarioManager

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'nickname', 'password']

    def save(self, commit=True):
        # Agora o super() vai encontrar o método save do ModelForm
        user = super(RegistrarForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user