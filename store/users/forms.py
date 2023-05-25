from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',    
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrForm(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',    
        'placeholder': 'Введите имя'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',    
        'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',    
        'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',    
        'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',    
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control py-4',    
    'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False) # Поле не обязательное для заполнения
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 
        'readonly': True})) # 'readonly': True - не для сохранения а для чтения
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'readonly': True}))
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'image', 'username', 'email']
