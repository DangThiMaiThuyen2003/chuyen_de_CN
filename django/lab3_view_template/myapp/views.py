import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404

# View hiển thị thời gian hiện tại
def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html lang='en'><body><h2>It is now {now}.</h2></body></html>"
    return HttpResponse(html)

# View trả về 404 bằng HttpResponseNotFound
def simple_404_view(request):
    return HttpResponseNotFound("<h1>Page not found</h1>")

# View raise Http404 (cách chuẩn Django)
def raise_404_view(request):
    raise Http404("This page does not exist")

# View trả về HTTP 201 Created
def created_view(request):
    return HttpResponse("<h1>Resource created successfully</h1>", status=201)
