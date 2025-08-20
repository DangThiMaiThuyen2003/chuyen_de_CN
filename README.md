# Django Models Practice  

## Task 1: Creating Simple Models  

- **Mục tiêu**: Thiết kế và triển khai các mô hình Django cho các thực thể như `Person`, `Group`, và `Membership`.  
- **Triển khai**: Định nghĩa các mô hình với các trường và mối quan hệ phù hợp để thể hiện các thực thể và tương tác của chúng.  

---

## Task 2: Querying Relationships và Complex Queries  

### Relational Queries  
- Thực hành truy vấn mối quan hệ giữa các mô hình `Blog`, `Author`, và `Entry`.  
- Lấy các đối tượng liên quan và lọc theo các điều kiện cụ thể.  

### Complex Queries  
- Sử dụng đối tượng `Q` của Django để thực hiện các truy vấn nâng cao với các điều kiện kết hợp (`AND`, `OR`, `NOT`) trên dữ liệu `Blog`, `Author`, và `Entry`.  

---

## Task 3: Writing Migrate (Forward) and Rollback (Backward) with Data  

### Forward Migration  
- Sử dụng `RunPython` với hàm `forwards_func` để chèn dữ liệu mẫu cho các mô hình `Blog`, `Author`, và `Entry`.  
- **Kết quả**: Thêm dữ liệu thành công, được xác minh qua Django shell sau khi chạy:  

```bash
python manage.py migrate
```

### Backward Migration  

- Sử dụng `filter` và `delete` với `schema_editor.connection.alias` để đảm bảo khả năng khôi phục.  
- **Kết quả**: Xóa dữ liệu thành công, được xác minh qua Django shell sau khi chạy:  

```bash
python manage.py migrate myapp 0011
```
## Task 4: Creating a Management Command for Sample Data Generation  

- **Implementation**: Tạo một custom management command tên `generate_sample_data` để sinh dữ liệu mẫu.  
- **Usage**:  

```bash
python manage.py generate_sample_data 2
```

Lệnh trên sẽ tạo 2 records per model `Blog`, `Author`, và `Entry`.

- **Verification**: Kiểm tra trong **Django shell** để xác nhận có 2 bản ghi cho mỗi model.

**Extra Task: Simple Interface Features**
Các Tính năng Triển khai:
- Thêm bài đăng mới với các trường tiêu đề, nội dung, ngày xuất bản, blog và tác giả.
- Hiển thị danh sách các bài đăng.
- Xem chi tiết bài đăng với đầy đủ thông tin.
- Xóa bài đăng.
- Xem chi tiết tác giả cùng với các bài đăng của họ.

**Setup Instructions**
1.	Set Up a Virtual Environment:
```bash
python -m venv venv
```
On Windows: ``` venv\Scripts\activate ```

2.	Install Dependencies:
```bash
pip install -r requirements.txt
```
3.	Apply Migrations:
```bash
python manage.py migrate
```
4.	Generate Sample Data:
```bash
python manage.py generate_sample_data 2
```
Sử dụng –delete flag để xóa dữ liệu mẫu hiện có:
```bash
python manage.py generate_sample_data 2 --delete
```
5.	Run the Development Server:
```bash
python manage.py runserver
```
Truy cập ứng dụng tại:  http://127.0.0.1:8000.

6.	Verify Data in Django Shell:
```bash
python manage.py shell
```
