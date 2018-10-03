from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from home.models import User

class UserCreationForm(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)

    class Meta:

        model = User

        # Note - include all *required* MyUser fields here,
        # but don't need to include password and confirm_password as they are
        # already included since they are defined above.
        fields = ('email', 'password', 'confirm_password')
    
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            self.add_error('confirm_password', 'Password & Confirm Password must match.')
        elif self.cleaned_data['email'][-11:] != 'handong.edu' :
            self.add_error('email', 'email은 한동계정만 사용가능합니다.')

        return super().clean()



    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user
