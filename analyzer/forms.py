from django import forms


class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 150,
            "cols": 20,
            "placeholder": "Text"
        }),
        required=True)