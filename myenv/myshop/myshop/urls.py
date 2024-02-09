from django.contrib import admin
from django.urls import path, include
from . import views  # upewnij się, że importujesz widoki z katalogu głównego

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', views.home, name='home'),  # to odpowiada za stronę główną
]
