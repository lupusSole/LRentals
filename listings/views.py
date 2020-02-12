from django.shortcuts import render, get_object_or_404
from .models import Listing

# Create your views here.

def home(req):
    listings = Listing.objects.all()[:3]
    return render(req, 'listings/home.html', {'listings':listings})

def all_listings(req):
    listings = Listing.objects.all()
    return render(req, 'listings/all.html', {'listings':listings}) 

def available(req):
    listings = Listing.objects.all().order_by('-dateAvailable')
    # change to after date added   listings = Listing.objects.order_by('-date')
    return render(req, 'listings/available.html', {'listings':listings})  

def detail(req, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(req, 'listings/detail.html', {'listing': listing} ) 
