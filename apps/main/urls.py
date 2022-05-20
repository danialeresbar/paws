from django.urls import path

from apps.main.views import DashboardRedirectView, SamplePAWSResponseView


urlpatterns = [
    path('', DashboardRedirectView.as_view(), name='dashboard'),
    path('sample/', SamplePAWSResponseView.as_view(), name='sample-response')
]
