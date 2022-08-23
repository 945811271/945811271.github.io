from django.http import HttpResponse
from django.template import loader


def test_html(request):
    t = loader.get_template('index.html')
    html = t.render()
    return HttpResponse(html)
