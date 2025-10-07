from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2  # Số items trên mỗi trang
    page_size_query_param = 'page_size'  # Cho phép client thay đổi số items/trang
    max_page_size = 100  # Giới hạn tối đa items/trang

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    default_limit = 2  # Số items mặc định trên mỗi trang
    max_limit = 100  # Giới hạn tối đa items có thể request