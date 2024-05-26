from django import forms
from .models import Employee, Role

class ItemForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['dept', 'role', 'first_name','last_name','salary','bonus','phone','hire_date']
        print("role")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("role")
        self.fields['role'].queryset = Role.objects.none()

        if 'dept' in self.data:
            try:
                print("bye")
                dept_id = int(self.data.get('dept'))
                self.fields['role'].queryset = Role.objects.filter(dept_id=dept_id).order_by('name')
            except (ValueError, TypeError):
                print("hi")
                pass  # invalid input from the client; ignore and fallback to empty SubCategory queryset

        elif self.instance.pk:
            print('tj')
            self.fields['role'].queryset = self.instance.dept.role_set.order_by('name')