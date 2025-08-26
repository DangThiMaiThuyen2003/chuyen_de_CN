import asyncio
import datetime
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Book
from django.views.generic import ListView

# Class-based view cơ bản với TemplateView
class AboutView(TemplateView):
    template_name = "cbvapp/about.html"


# Class-based async view
class AsyncHelloView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)  # mô phỏng xử lý bất đồng bộ
        return HttpResponse("<h1>Hello async world!</h1>")
    
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"  # template để render GET

    # xử lý HTTP HEAD request
    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            headers={
                "Last-Modified": last_book.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            }
        )
        return response

