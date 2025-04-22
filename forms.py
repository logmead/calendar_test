from django import forms

class CalendarForm(forms.Form):

    date_field = forms.DateField(label="")

