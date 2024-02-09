from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),

]
