from django import forms
from portal.models import Post, Bids

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author','title', 'vehicle_model', 'vehicle_age','vehicle_km', 'vehicle_image', 'text', 'vr_image']

        widget = {
            'title': forms.TextInput(attrs={'class':'textInputClass editable medium-editor-textarea'}),
            'vehicle_model': forms.TextInput(attrs={'class': 'textInputClass medium-editor-textarea'}),
            'vehicle_age': forms.TextInput(attrs={'class': 'editable medium-editor-textarea'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textareaa'}),



        }

class BidForm(forms.ModelForm):

    class Meta:
        model = Bids
        fields = ['bidder', 'bid_amount']

        widgets = {





        }
