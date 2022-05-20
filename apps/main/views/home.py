from django.http import JsonResponse
from django.views import View
from django.views.generic.base import RedirectView
from rest_framework import status


SAMPLE_PAWS_RESPONSE = {
        "jsonrpc": "2.0",
        "method": "spectrum.paws.getSpectrum",
        "params": {
            "type": "AVAIL_SPECTRUM_REQ",
            "version": "1.0",
            "deviceDesc": {
                "serialNumber": "XXX",
                "fccId": "YYY",
                "rulesetIds": ["FccTvBandWhiteSpace-2010"]
            },
            "location": {
                "point": {
                    "center": {
                        "latitude": 2.0, "longitude": 2123
                    }
                }
            },
            "antenna": {
                "height": 10.2, "heightType": "AGL"
            }
        },
        "id": str(123213)
    }


class DashboardRedirectView(RedirectView):

    pattern_name = 'admin:index'

    def get_redirect_url(self, *args, **kwargs):
        """
        Check the headers to redirect to the administration dashboard
        or the API documentation
        """

        return super(DashboardRedirectView, self).get_redirect_url()


class SamplePAWSResponseView(View):

    def get(self, request):
        return JsonResponse(
            SAMPLE_PAWS_RESPONSE,
            status=status.HTTP_200_OK
        )
