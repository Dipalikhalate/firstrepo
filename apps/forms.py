from django import forms
from .models import Post, Category

# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'),]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')

        widgets = {
          'title': forms.TextInput(
              attrs={
                  'class': 'form-control'
              }
          ),
           'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title placeholder Stuff'}),
           'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'elder'}),
           'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
           'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),



        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title placeholder Stuff'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),


        }
