from django import forms

from portfolio.models import ImageElement, PortfolioMediaElement, PortfolioPiece, TextElement, VideoElement


class PortfolioPieceForm(forms.ModelForm):
    class Meta:
        model = PortfolioPiece
        fields = ["title", "description", "tags", "thumbnail", "status"]


class SingleImageElementForm(forms.ModelForm):
    class Meta:
        model = ImageElement
        fields = ["img", "caption", "order", "temp"]


class MultipleImageElementForm(forms.ModelForm):
    imgs = forms.FileField(widget = forms.TextInput(
                                    attrs={
                                        "name": "images",
                                        "type": "File",
                                        "multiple": "True",}
                                        ),
                           label = "",
                           required=False
                           )
    class Meta:
        model = ImageElement
        fields = ["imgs"]


class VideoElementForm(forms.ModelForm):
    class Meta:
        model = VideoElement
        fields = ["video", "caption"]


class TextElementForm(forms.ModelForm):
    class Meta:
        model = TextElement
        fields = ["text"]


class PortfolioMediaElementForm(forms.ModelForm):
    class Meta:
        model = PortfolioMediaElement
        fields = ["element_type", "image", "video", "text", "caption", "order"]


PortfolioMediaElementFormset = forms.inlineformset_factory(PortfolioPiece, PortfolioMediaElement,
                                                           form=PortfolioMediaElementForm, extra=1, can_delete=True)

ImageElementFormset = forms.inlineformset_factory(PortfolioPiece, ImageElement,
                                                  form=SingleImageElementForm, extra=1, can_delete=True)
VideoElementFormset = forms.inlineformset_factory(PortfolioPiece, VideoElement,
                                                  form=VideoElementForm, extra=1, can_delete=True)
TextElementFormset = forms.inlineformset_factory(PortfolioPiece, TextElement,
                                                  form=TextElementForm, extra=1, can_delete=True)
