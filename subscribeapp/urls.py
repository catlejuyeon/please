from django.urls import path

from subscribeapp.views import SubscriptionView, SubScriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubScriptionListView.as_view(), name='list'),
]
