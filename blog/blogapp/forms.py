from django import forms
from .models import Post

class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')

class Anketa(forms.Form):
    name = forms.CharField(label='Имя')
    lname = forms.CharField(label='Фамилия')
    adres = forms.CharField(label='Адрес')
    sex = forms.ChoiceField(label='Пол', choices=[('M', 'Мужской'), ('F', 'Женский')])
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')
    favorite_book = forms.CharField(label='Любимая книга')
    favorite_movie = forms.CharField(label='Любимый фильм')

# class SearchForm(forms.Form):
#     q = forms.CharField(label='Поиск')

class SearchForm(forms.Form):
    q = forms.CharField(label='Поиск')