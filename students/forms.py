from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["roll_number", "full_name", "email", "phone", "department", "year"]
        widgets = {
            "roll_number": forms.TextInput(attrs={"placeholder": "e.g. 23CS001"}),
            "full_name": forms.TextInput(attrs={"placeholder": "Enter full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "student@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "department": forms.TextInput(attrs={"placeholder": "e.g. Computer Science"}),
            "year": forms.Select(),
        }

    def clean_roll_number(self):
        value = self.cleaned_data["roll_number"].strip().upper()
        qs = Student.objects.filter(roll_number=value)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This roll number is already registered.")
        return value

    def clean_email(self):
        value = self.cleaned_data["email"].strip().lower()
        qs = Student.objects.filter(email=value)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This email is already registered.")
        return value
