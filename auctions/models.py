from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from urllib import request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.forms.fields import CharField, DateTimeField
from PIL import Image
import datetime
import pytz
from django.db.models.query_utils import DeferredAttribute

from django.utils import timezone
import time

class User(AbstractUser):
    pass


class ItemListing(models.Model):
    seller = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name="saleItems")
    name = models.CharField(max_length=64)
    img = models.ImageField(upload_to ='images/')
    description = models.CharField(max_length=10000)
    auctionStart = models.DateTimeField(blank=True, default=datetime.datetime.utcnow)
    auctionEnd = models.DateTimeField(null=True, blank=True)
    startingBid = models.DecimalField(null=True, blank=True, max_digits=128, decimal_places=2)
    """bids = models.ForeignKey('Bid', on_delete=models.DO_NOTHING, related_name="item")"""
    highestBid = models.ForeignKey('Bid', null=True, blank=True, on_delete=models.DO_NOTHING)

    def is_active(self):
        now = datetime.datetime.now(timezone.utc).replace(microsecond=0)
        hour = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=1, weeks=0)
        if self.auctionStart < now  < self.auctionEnd:
            return True
        else:
            self.close_item_check
            return False

    def going_live(self):
        now = datetime.datetime.now(timezone.utc).replace(microsecond=0)
        if self.auctionStart > now:
            return True
        else:
            return False

    def has_ended(self):
        now = datetime.datetime.now(timezone.utc).replace(microsecond=0)
        if now > self.auctionEnd:
            return True
        else:
            return False        

    def get_last_6(self):
        bids = Bid.objects.filter(bidItem=self).order_by('-bidPlaced')[:6:-1]
        return bids

    def get_remain(self):
        now = time.time()
        print("This RAN")
        print(now)
        end_time = self.auctionEnd
        time_left = (end_time.timestamp())
        print(time_left)
        milliseconds_left = time_left - now
        return round(milliseconds_left/1000)

    def is_unwatched(self):
        print("Made it here at least")
        list = []
        if len(list) == 0:
            print("There is list")
            print(list)
        else:
            print("no list")
            print(list)
        if self in list:
            print("We False Here")
            return False
        else:
            print("We True Here")
            return True

    def unwatched(self):
        list=self.watching.all()
        current_user = request.user
        print(current_user)
        print("hello")
        print(j)
        for i in list:
            if i == request.User.profile:
                return False
            else:
                return True

    """DEFUNCT"""

    def close_item_check(self):
        now = datetime.datetime.now(timezone.utc).replace(microsecond=0)
        if now > self.auctionEnd:
            if self.winningBid == None:
                self.winningBid = self.highestBid
        else:
            pass

class Bid(models.Model):
    bid = models.DecimalField(max_digits=128, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bidItem = models.ForeignKey(ItemListing, related_name="bids", on_delete=models.CASCADE)
    bidPlaced = models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))

    """def highest_bid(self):
        highest = None
        if self.bids == None:
            return False
        else:
            for i in self.bids:
                if i.bid > highest.bid:
                    highest = i
                else:
                    pass
        return highest"""

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first = models.CharField(max_length=64)
    lasts = models.CharField(max_length=64)
    profile_pic = models.ImageField(upload_to ='images/')
    description = models.CharField(max_length=10000)
    watchlist = models.ManyToManyField(ItemListing, blank=True, null=True, related_name="watching")

    def get_items(self):
        person = self.owner
        items = ItemListing.objects.filter(seller=person)
        return items

class Comment(models.Model):
    comment = models.TextField()
    commentter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="userComments")
    commentItem = models.ForeignKey(ItemListing, on_delete=models.CASCADE,null=True, blank=True, related_name="itemComments")
    commentProfile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name="profileComments")

    """class rating(models.IntegerChoices):
        Rubbish = 1
        Meh = 2
        Trouble ="""