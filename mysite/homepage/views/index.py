from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone, timedelta

@view_function
def process_request(request):
    # delta = timedelta(hours=hrs, minutes=mins)
    # now = datetime.now()
    # now = now + delta if delta else now - delta

    context = {
        jscontext('now'): datetime.now(),
    }

    return request.dmp.render('index.html', context)


@view_function
def gettime(request):
    context = {
        'now': datetime.now(),
    }
    return request.dmp.render('index.gettime.html', context)