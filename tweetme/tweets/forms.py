from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                widget=forms.Textarea(
                        attrs={'placeholder': "Your message",
                            "class": "form-control","maxlength":"140"}
                    ))
    class Meta:
        model=Tweet
        fields = [
            # "user",
            "content"
        ]
    #we can define validators in forms or in models itself
    #clean_(formfield) is defined
    def clean_content(self,*args,**kwargs):
        content = self.cleaned_data.get("content")
        if content == 'abc':
            raise forms.ValidationError("Dont enter abc")
        return content
