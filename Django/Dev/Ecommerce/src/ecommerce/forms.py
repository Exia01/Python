from django import forms
from .emailTypes import approvedEmails


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_full_name', "placeholder": "Your full name", }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control", 'id': 'form_email', "placeholder": "Your email", }))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", 'id': 'form_contact_message', "placeholder": "Your message", }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        temp_email = email.split('@')[1]

        if temp_email not in approvedEmails:
            raise forms.ValidationError("Email has to be valid..see list.")

        return email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is wrong.")


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_username', "placeholder": "Your Username", }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control", 'id': 'form_password' }))