from django import forms
#from .models import Customer

# class InputForm1(forms.Form):
#           name = forms.CharField()
#           email = forms.EmailField()
#           password = forms.CharField()
# class SignupForm(forms.Form):
#         username = forms.CharField()
#         email = forms.EmailField()
#         password = forms.CharField()  
# class CustomerForm(forms.ModelForm):
#         class Meta:
#                 model = Customer
#                 fields = '__all__'
class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField() 
