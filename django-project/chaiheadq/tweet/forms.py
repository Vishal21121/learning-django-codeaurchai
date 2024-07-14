from django import forms
from models import Tweet

# here we are using django's Form we can use our custom form as well
class TweetForm(forms.ModelForm):
    # It is mandatory to create this class
    class Meta:
        model = Tweet
        # this text and photo is the from the Tweet model already created
        fields = ['text','photo']