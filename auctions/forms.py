from dataclasses import fields
from django import forms
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.core.validators import *
from .models import *
import urllib.request

class NewListingModel(ModelForm):
    class Meta:
        model = ItemListing
        fields = '__all__'

class NewBidModel(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']

    def __init__(self, *args, **kwargs):
        print("init happen here, innit!")
        print(args)
        print("this is the kwargs!")
        print(kwargs)
        if args:
            unpack = args[0]
            id = unpack.get('id')
            next = unpack.get('next')
            print(next)
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
        print(bid)
        print(item)
        print("check at least ran")
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