# -*- coding: utf-8 -*-
from django import forms

__author__ = 'mario'

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
