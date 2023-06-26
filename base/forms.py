from django import forms
from . models import *

# TypeWritter
class TypeWritterForm(forms.ModelForm):
    class Meta:
        model = TypeWritter
        fields = "__all__"
        widgets = {
            'text':forms.TextInput(attrs=({'placeholder':'Write Text...', 'class':'custom-input'})),
        }
        
### Facts
class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = "__all__"
        widgets = {
            'fact_description':forms.Textarea(attrs=({'placeholder':'Description...', 'class':'cumtom-input'})),
            'happy_client':forms.NumberInput(attrs=({'placeholder':'Happy Client Number...', 'class':'custom-input'})),
            'project':forms.NumberInput(attrs=({'placeholder':'Projects Number...', 'class':'custom-input'})),
            'cup_of_coffee':forms.NumberInput(attrs=({'placeholder':'Cup Of Coffee Number...', 'class':'custom-input'})),
            'award':forms.NumberInput(attrs=({'placeholder':'Awards Number...', 'class':'custom-input'})),
            
        }

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
        
        
# Skill
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'Enter Subject Name...', 'class':'custom-input'})),
            'skill':forms.NumberInput(attrs=({'placeholder':'Enter Skill percents(%)...', 'class':'custom-input'})),
        }
        
# Gallery
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        widgets = {
            'subject':forms.Select(attrs=({'class':'custom_input'})),
            'image':forms.FileInput(attrs=({'placeholder':'Choice image...', 'class':'custom-input'})),
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
        
# My Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'Enter Your Name...', 'class':'custom-input'})),
            'email':forms.EmailInput(attrs=({'placeholder':'Enter Your Email...', 'class':'custom-input'})),
            'subject':forms.TextInput(attrs=({'placeholder':'Enter Subject...', 'class':'custom-input'})),
            'message':forms.Textarea(attrs=({'placeholder':'Write Message...', 'class':'custom-input'})),
            
        }