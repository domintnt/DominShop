from django.shortcuts import render


def payment_process(request):
    return render(request, 'payment/process.html')


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
