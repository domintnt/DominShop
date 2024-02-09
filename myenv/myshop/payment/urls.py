from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='payment_process'),
    path('done/', views.payment_done, name='payment_done'),
    path('canceled/', views.payment_canceled, name='payment_canceled'),

]
