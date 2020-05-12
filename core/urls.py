from django.urls import path
from .views import (
    products,
    checkout,
    home
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    #path('', HomeView.as_view(), name='home'),
    # have to call as_view() function so as to return a callable view that takes a request and returns a response.
    # as_view() - Its the main entry-point in request-response cycle in case of generic views
    path('checkout/', checkout, name="checkout"),
    path('products/', products, name="products")
]
