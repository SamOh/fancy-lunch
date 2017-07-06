from django.http import HttpResponse
from django.template.loader import get_template
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('base.html')
    html = t.render({
        'now': now
    })
    return HttpResponse(html)