# Chuyên đề Công nghệ - Django Framework

Django là một **framework web mạnh mẽ bằng Python** giúp phát triển ứng dụng web nhanh chóng, an toàn và dễ bảo trì. Django hỗ trợ quản lý database thông qua ORM, xây dựng các view, template, và tích hợp sẵn admin interface để quản lý dữ liệu.

---

**Hướng dẫn chạy dự án**

**1. Tạo và kích hoạt môi trường ảo (Virtual Environment)**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
``` 

**2. Tạo dự án Django**

```bash
django-admin startproject <ten_du_an>
cd <ten_du_an>
```

**3. Tạo ứng dụng Django**
```bash
python manage.py startapp <ten_ung_dung>
```

**4. Cài đặt các dependencies**
```bash
pip install -r requirements.txt
```

**5. Kết nối database**

Chỉnh sửa settings.py để kết nối database (PostgreSQL hoặc SQLite).

**6. Chạy migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**7. Tạo tài khoản admin**
```bash 
python manage.py createsuperuser
``` 

**8. Chạy server Django**
```bash
python manage.py runserver
```
Truy cập ứng dụng tại: http://127.0.0.1:8000/

Truy cập admin tại: http://127.0.0.1:8000/admin/



