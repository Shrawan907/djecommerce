from django.urls import path
from .views import (
    CheckoutView,
    ItemDetailView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    OrderSummary,
    remove_single_item_from_cart
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', HomeView.as_view(), name='home'),
    # have to call as_view() function so as to return a callable view that takes a request and returns a response.
    # as_view() - Its the main entry-point in request-response cycle in case of generic views
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('product/<slug>/', ItemDetailView.as_view(), name="product"),
    # the reason it is taken <slug> because it is DetailView so either we pass primary key or slug for class based view to handel which object it is getting

    path('order-summary/', OrderSummary.as_view(), name="order-summary"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
