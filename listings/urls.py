
from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
   path('', views.all_listings, name='all_listings'),
   path('available', views.available, name='available'),
   path('<int:listing_id>', views.detail, name='detail'),


]