from django import forms

from .models import Comment, Image
from django.shortcuts import render


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')


def ImageUploadView(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
        return render(request, 'index.html', {'form': form})