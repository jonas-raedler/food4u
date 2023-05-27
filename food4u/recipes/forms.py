from django import forms

class RecipeForm(forms.Form):

    name = forms.CharField(label="Name of Recipe", max_length=100, widget=forms.TextInput(attrs={"class": "form_item"}))
    ingredient = forms.CharField(label="Ingredient", max_length=150, widget=forms.TextInput(attrs={"class": "form_item"}))


class MyForm(forms.Form):
    original_field = forms.CharField()
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()