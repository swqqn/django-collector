from django.forms import Form, EmailField
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from collector.models import Blob


class CreateForm(Form):
    email = EmailField()


@require_http_methods(['POST'])
def create(request):
    data = request.POST

    form = CreateForm(data)
    if not form.is_valid():
        return HttpResponse(status=400)

    blob = Blob()
    blob.emal = data['email']

    blob.save()

    # TODO: send e-mail

    return HttpResponse(status=201)


@require_http_methods(['GET'])
def delete(request, uid):
    blob = get_object_or_404(Blob, uid=uid)
    blob.delete()

    return HttpResponse(status=204)


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
