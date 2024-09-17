from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'aria-describedby': 'usernameHelp',
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )
    remember_me = forms.BooleanField(
        label="Remember me",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    def as_bootstrap(self):
        return f"""
        <div class="form-group">
            <label for="id_username">{self['username'].label}</label>
            {self['username']}
            <small id="usernameHelp" class="form-text text-muted">We'll never share your username with anyone else.</small>
            {self.errors.get('username')}
        </div>
        <div class="form-group">
            <label for="id_password">{self['password'].label}</label>
            {self['password']}
            {self.errors.get('password')}
        </div>
        <div class="form-check">
            {self['remember_me']} {self['remember_me'].label}
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
        """


    
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
    
class UserEditForm(forms.ModelForm):
    
  class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        
        
class ProfileEditForm(forms.ModelForm):
 class Meta:
 
   model = Profile
   fields = ['date_of_birth', 'photo']    
 

