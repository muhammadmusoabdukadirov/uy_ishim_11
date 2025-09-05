from django import forms
from .models import Announcement

class NewsForm(forms.ModelForm):
    class Meta:
        model = Announcement
        exclude = ['views', 'create_at', 'update_at']
        labels = {
            "name": "Maqola nomi",
            "description": "Maqola tavsifi",
            "image": "Rasm yuklash",
            "video": "Video yuklash",
            "author": "Bo'limni tanlang",
            "published": "Saytga chiqarilsinmi?"
        }
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Maqola nomini kiriting",
                "style": "border-radius: 10px; padding: 10px"
            }),
            'description': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Maqola tavsifini kiriting",
                "rows": 5,
                "style": "border-radius: 10px; padding: 10px"
            }),
            'author': forms.Select(attrs={
                "class": "form-select",
                "style": "border-radius: 10px; padding: 10px"
            }),
            'published': forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }
