from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth. models import User

####### for Register #########
class RegisterForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'password1', 'password2']

   def __init__(self, *args, **kwargs):
      super(RegisterForm, self).__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Username.....'})
      self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter password.....'})
      self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Username.....'})