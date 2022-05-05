from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import DecimalField, ModelChoiceField, ModelForm, ValidationError
from django.core.validators import *
from .models import *
import urllib.request

class NewListingModel(ModelForm):
    class Meta:
        model = ItemListing
        fields = '__all__'

class NewBidModel(ModelForm):
    bid = DecimalField(
        min_value=0,
        decimal_places=2,
    )
    class Meta:
        model = Bid
        fields = ['bid']

    def __init__(self, *args, **kwargs):
        if args:
            unpack = args[0]
            id = unpack.get('id')
            item = ItemListing.objects.get(pk=id)
            self.bidItem = item
        super(NewBidModel, self).__init__(*args, **kwargs)
        """self.bidItem = ItemListing.objects.get(pk=self.number)
        self.fields['bidItem']=ItemListing.objects.filter(pk=4)
        data = self.fields.bidItem
        print(data)"""

    def clean(self, *arg, **kwargs):
        cleaned_data = super().clean()
        print("Got here clean_bid!")
        print(cleaned_data)
        bid = cleaned_data.get('bid')
        item = self.bidItem
        strBid = str(bid)
        print(strBid)
        print(item)
        print("check at least ran")

        """if '.' in strBid:
            print("decimal check working")
            if len(strBid) >= 17:
                raise ValidationError("Seems like a lot of cash!")
        else:
            if len(strBid) >= 16:
                raise ValidationError("Seems like a lot of cash!")"""
        if item.highestBid == None:
            if bid<=item.startingBid:
                raise forms.ValidationError("Please raise your bid")
            else:
                return cleaned_data
        else:
            if bid<=item.highestBid.bid:
                raise forms.ValidationError("Please raise your bid")
            else:
                print("the check cleared!")
                return cleaned_data