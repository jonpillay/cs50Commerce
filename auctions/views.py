from pickle import FALSE
from tkinter import Widget
from unittest.util import _MAX_LENGTH
from urllib import request
from django.core import validators
from auctions.forms import *

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms import *
from django.forms.fields import CharField
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from PIL import Image

from .models import *
from .models import User
from .utils import *

class SearchForm(forms.Form):
    search = forms.CharField()

def index(request):
    if request.method == 'POST':
        search = SearchForm(request.POST)
        if search.is_valid():
            word = search.cleaned_data['search'].lower()
            filenames = ItemListing.objects.all()
            for i in filenames:
                if word == i.name.lower():
                    return redirect("item", item_id=i.id)
                elif word in i.name.lower():
                    matches=[]
                    for q in filenames:
                            if word in q.name.lower():
                                matches.append(q)
                    return render(request, "auctions/partial-result.html", {
                            "word": word.capitalize(),
                            "matches": matches
                    })
            else:               
                return render(request, "auctions/not-found.html", {
                        "word": word.capitalize(),
                })
    now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
    form = NewBidModel
    return render(request, "auctions/index.html", {
        "items": ItemListing.objects.all(),
        "now": now,
        "bidForm": form,
        "searchform": SearchForm
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

class ProfileForm(forms.Form):
    first = forms.CharField(max_length=64, label="First Name: ")
    lasts = forms.CharField(max_length=64, label="Last Names: ")
    profile_pic = forms.ImageField(label="Show Us Yah Mug: ")
    description = forms.CharField(widget=forms.Textarea, label="About Yourself")

def new_comment(request, item_id=None, profile_id=None):
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise Http404
        if item_id == None:
            form = CommentForm(request.POST)
            if form.is_valid():
                commentter = request.user
                commentProfile = Profile.objects.get(pk=profile_id)
                comment = form.cleaned_data["comment"]
                obj = Comment.objects.create(
                    commentter = commentter,
                    commentProfile= commentProfile,
                    comment = comment
                )
                obj.save()
                return redirect('profile', user_id=commentProfile.id)
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                commentter = request.user
                commentItem = ItemListing.objects.get(pk=item_id)
                comment = form.cleaned_data["comment"]
                obj = Comment.objects.create(
                    commentter = commentter,
                    commentItem= commentItem,
                    comment = comment
                )
                obj.save()
                return redirect('item', item_id=commentItem.id)

def create_profile(request, user_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise Http404
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            owner = request.user
            first = form.cleaned_data["first"]
            lasts = form.cleaned_data["lasts"]
            profile_pic = form.cleaned_data["profile_pic"]
            description = form.cleaned_data["description"]
            obj = Profile.objects.create(
                owner = owner,
                first = first,
                lasts = lasts,
                profile_pic = profile_pic,
                description = description
            )
            obj.save()
            profile = Profile.objects.get(pk=user_id)
            return render(request, "auctions/profile.html",{
                "profile": profile
            })
        else:
            raise Http404
    else:    
        if request.user.id == user_id:
            return render(request, "auctions/new_profile.html", {
                "profile_form": ProfileForm,
            })
        else:
            raise Http404

def profile(request, user_id):
    profile = Profile.objects.get(pk=user_id)
    now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
    return render(request, "auctions/profile.html",{
        "profile": profile,
        "now": now,
        "commentForm": CommentForm,
        "bidForm": NewBidForm, 
    })

class NewListingForm (forms.Form):
    itemName = forms.CharField(max_length=128, label="What's that then?")
    itemDescript = forms.CharField(widget=forms.Textarea, label="Tel us about it")
    itemImage = forms.ImageField(label="Show us a photo")
    startingBid = forms.DecimalField(decimal_places=2, label="What is your starting bid?")
    auctionStart = forms.DateTimeField(label="Auction Start", widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}))
    auctionEnd = forms.DateTimeField(label="Auction End", widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}))

def new_listing(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise Http404
        form = NewListingForm(request.POST, request.FILES)
        if form.is_valid():
            seller = request.user
            name = form.cleaned_data["itemName"]
            description = form.cleaned_data["itemDescript"]
            img = form.cleaned_data["itemImage"]
            startingBid = form.cleaned_data["startingBid"]
            auctionStart = form.cleaned_data["auctionStart"]
            auctionEnd = form.cleaned_data["auctionEnd"]
            obj = ItemListing.objects.create(
                name = name,
                description = description,
                img = img,
                seller = seller,
                auctionStart = auctionStart,
                auctionEnd = auctionEnd,
                startingBid = startingBid
            )
            obj.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            raise Http404
    else:
        return render(request, "auctions/new_listing.html", {
            "form": NewListingForm,
    })

class NewBidForm(forms.Form):
    bid = forms.DecimalField(decimal_places=2, label="Place bid")

def test_form(request, item_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
            return render(request, "auctions/index.html", {
                "items": ItemListing.objects.all(),
                "now": now,
                "bidForm": NewBidForm,
                "message": "Please login in to Bid!"
            })
        form = NewBidModel(request.POST)
        if form.is_valid():
            print("form was valid")
            print(form)
            bid = form.cleaned_data['bid']
            bidItem = ItemListing.objects.get(pk=item_id)
            bidder = request.user
            if bidder == bidItem.seller:
                now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
                return render(request, "auctions/index.html", {
                    "items": ItemListing.objects.all(),
                    "now": now,
                    "bidForm": NewBidForm,
                    "message": "No Bid Rigging"
                })
            if bidItem.is_active():
                if bidItem.highestBid == None:
                    if bid > bidItem.startingBid:
                        obj = Bid.objects.create(
                                bid = bid,
                                bidder = bidder,
                                bidItem = bidItem
                            )
                        obj.save()
                        print("this " + obj.bidItem.name)
                        bidItem.highestBid = obj
                        bidItem.save(update_fields=['highestBid'])
                        return HttpResponseRedirect(reverse("index"))
                    else:
                        pass
                else:
                    if bid > bidItem.highestBid.bid:
                        obj = Bid.objects.create(
                            bid = bid,
                            bidder = bidder,
                            bidItem = bidItem
                        )
                        obj.save()
                        bidList = Bid.objects.filter(bidItem=bidItem)
                        print(bidList)
                        bidItem.bids.add(obj)
                        bidList = Bid.objects.filter(bidItem=bidItem)
                        print(bidList)
                        bidItem.highestBid = obj
                        bidItem.save(update_fields=['highestBid'])
                        return HttpResponseRedirect(reverse("index"))
                    else:
                        now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
                        return render(request, "auctions/index.html", {
                            "items": ItemListing.objects.all(),
                            "now": now,
                            "bidForm": NewBidModel,
                            "message": "Not High Enough Buddy"
                        })
            else:
                print("item is_active check working")
                return HttpResponseRedirect(reverse("index"))
        else:
            """When rerendering the page for the index, see if you can reinsert the error message relating to the item_id...
            so it renders on the corrent form"""
            now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
            return render(request, "auctions/validator_test.html", {
            "bidForm": form,
            "now": now,
        })
    else:
        now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
        return render(request, "auctions/validator_test.html", {
        "bidForm": NewBidForm,
        "now": now,
    })

def new_bid(request, item_id):
    if request.method == "POST":
        form = NewBidModel(request.POST)
        if not request.user.is_authenticated:
            now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
            return render(request, "auctions/index.html", {
                "items": ItemListing.objects.all(),
                "now": now,
                "bidForm": NewBidForm,
                "message": "Please login in to Bid!"
            })
        if form.is_valid():
            print("form was valid")
            bid = form.cleaned_data['bid']
            bidItem = ItemListing.objects.get(pk=item_id)
            bidder = request.user
            if bidder == bidItem.seller:
                now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
                return render(request, "auctions/index.html", {
                    "items": ItemListing.objects.all(),
                    "now": now,
                    "bidForm": NewBidModel,
                    "message": "No Bid Rigging"
                })
            if bidItem.is_active():
                if bidItem.highestBid == None:
                    if bid > bidItem.startingBid:
                        obj = Bid.objects.create(
                                bid = bid,
                                bidder = bidder,
                                bidItem = bidItem
                            )
                        obj.save()
                        print("this " + obj.bidItem.name)
                        bidItem.highestBid = obj
                        bidItem.save(update_fields=['highestBid'])
                        if 'nextCont' not in locals():
                            return HttpResponseRedirect(next)
                        else:
                            return HttpResponseRedirect(nextCont)
                else:
                    if bid > bidItem.highestBid.bid:
                        obj = Bid.objects.create(
                            bid = bid,
                            bidder = bidder,
                            bidItem = bidItem
                        )
                        obj.save()
                        bidList = Bid.objects.filter(bidItem=bidItem)
                        print(bidList)
                        bidItem.bids.add(obj)
                        bidList = Bid.objects.filter(bidItem=bidItem)
                        print(bidList)
                        bidItem.highestBid = obj
                        bidItem.save(update_fields=['highestBid'])
                        print("Got this far with the bug")
                        print(request.POST)
                        next = request.POST.get('page', '/')
                        if 'item' in next:
                            print(next)
                            return HttpResponseRedirect(reverse(next, args=[item_id]))
                        else:
                            return HttpResponseRedirect(reverse(next))
                    else:
                        now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
                        return render(request, "auctions/index.html", {
                            "items": ItemListing.objects.all(),
                            "now": now,
                            "bidForm": NewBidModel,
                            "message": "Not High Enough Buddy"
                        })
            else:
                print("item is_active check working")
                return HttpResponseRedirect(reverse("index"))
        else:
            print("Why the fuck is next not updating?")
            next = request.POST.get('page', '/')
            print("this is next the python variable" + next)
            errorID = item_id
            now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
            if "item" in next:
                print("Check for item word worked")
                item = ItemListing.objects.get(id=item_id)
                return render(request, "auctions/item.html", {
                        "item": item,
                        "items": ItemListing.objects.all(),
                        "now": now,
                        "errorID": errorID,
                        "errorForm": form,
                        "bidForm": NewBidModel,
                    })
            else:
                return render(request, "auctions/index.html", {
                        "items": ItemListing.objects.all(),
                        "now": now,
                        "errorID": errorID,
                        "errorForm": form,
                        "bidForm": NewBidModel,
                    })

def item_page(request, item_id, error_form=None):
    errorID = item_id
    item = ItemListing.objects.get(id=item_id)
    now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
    return render(request, "auctions/item.html", {
        "item": item,
        "commentForm": CommentForm,
        "bidForm": NewBidModel,
        "now": now,
        "end": item.auctionEnd.timestamp(),
        "errorID": errorID,
        "errorForm": error_form
    })

def close_item(request, item_id):
    item = ItemListing.objects.get(pk=item_id)
    now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise Http404
        if request.user == item.seller:
            item.auctionEnd = now
            item.save()
            return redirect('item', item_id=item.id)
        else:
            raise Http404

def watch(request, item_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise Http404
        item = ItemListing.objects.get(pk=item_id)
        profile = Profile.objects.get(pk=int(request.user.id))
        profile.watchlist.add(item)
        print("Success!!!")
        return HttpResponseRedirect(reverse('index'))

def unwatch(request, item_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            raise Http404
        item = ItemListing.objects.get(pk=item_id)
        profile = Profile.objects.get(pk=int(request.user.id))
        profile.watchlist.remove(item)
        print("Success!!!")
        return HttpResponseRedirect(reverse('index'))

def watchlist(request):
    now = pytz.utc.localize(datetime.datetime.utcnow().replace(microsecond=0))
    profile = request.user.profile
    watchlist = profile.watchlist.all()
    if watchlist == None:
        message = "Not Watching Anything"
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist,
        "now": now,
        "bidForm": NewBidForm,
    })