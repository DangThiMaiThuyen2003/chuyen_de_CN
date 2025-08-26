from django.http import HttpResponse

def special_case_2003(request):
    return HttpResponse("Năm đặc biệt: 2003")

def year_archive(request, year):
    return HttpResponse(f"Trang lưu trữ năm: {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Trang lưu trữ tháng: {month}/{year}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Bài viết: {slug}, tháng {month}, năm {year}")
