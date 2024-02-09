from django.contrib import admin
from django.urls import path, include
from . import views  # upewnij się, że importujesz widoki z katalogu głównego

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', views.home, name='home'),
]
