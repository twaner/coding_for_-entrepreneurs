__author__ = 'taiowawaner'

from joins.models import Join
from django.core.exceptions import ObjectDoesNotExist


class ReferMiddleWare():
    @classmethod
    def process_request(self, request):
        """
        middleware method to get the ref id of a user and assign it to a session variable.
        :param request: http request.
        """
        ref_id = request.GET.get("ref")
        try:
            obj = Join.objects.get(ref_id=ref_id)
        except ObjectDoesNotExist:
            obj = None

        # Set session variable of ref to the object's id.
        if obj:
            request.session['join_id_ref'] = obj.id