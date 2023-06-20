from django import forms
from . models import *

##### About
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"
        
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'Name...', 'class':'cumtom-input'})),
            'birthday':forms.DateInput(attrs=({'placeholder':'Birthday...', 'class':'cumtom-input', 'type':'date'})),
            'email':forms.TextInput(attrs=({'placeholder':'Email...', 'class':'cumtom-input'})),
            'phone':forms.TextInput(attrs=({'placeholder':'Phone...', 'class':'cumtom-input'})),
            'description':forms.Textarea(attrs=({'placeholder':'Description...', 'class':'cumtom-input'})),
        }
        
# TypeWritter
class TypeWritterForm(forms.ModelForm):
    class Meta:
        model = TypeWritter
        fields = "__all__"
        widgets = {
            'text':forms.TextInput(attrs=({'placeholder':'Write Text...', 'class':'custom-input'})),
        }
        
# Skill
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'Enter Subject Name...', 'class':'custom-input'})),
            'skill':forms.NumberInput(attrs=({'placeholder':'Enter Skill percents(%)...', 'class':'custom-input'})),
        }
        
        
        
# My Blog
class MyBlogForm(forms.ModelForm):
    class Meta:
        model = MyBlog
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs=({'placeholder':'Write Title...', 'class':'custom-input'})),
            'description':forms.Textarea(attrs=({'placeholder':'Write Description...', 'class':'custom-input'})),
            'image':forms.FileInput(attrs=({ 'class':'custom-input'})),
            
        }