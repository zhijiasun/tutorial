from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Fieldset,HTML

class Contact(forms.Form):
	subject = forms.CharField()
	message = forms.CharField(max_length=100)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)


class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
            label = "Do you like this website",
            choices = ((1,"Yes"),(2,"NO")),
            coerce = lambda x: bool(int(x)),
            widget = forms.RadioSelect,
            initial = '1',
            required = True,
        )

    favourite_food = forms.CharField(
            label = "What is your favourite food?",
            max_length = 80,
            required = True,
        )

    favourite_color = forms.CharField(
            label = "What is your favourite color?",
            max_length = 80,
            required = True,
        )


    def __init__(self,*args,**kwargs):
        super(ExampleForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit','Submit'))
        self.helper.layout = Layout(
                Fieldset(
                    'First arg is the legend of the fieldset',
                    'like_website',
                    'favourite_color', #this is the field name of the form
                    HTML("""
                        <p> here we can insert some html doc <strong>Such As</strong></p>
                    """),
                    'favourite_food',
                    )
                )
