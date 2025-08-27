Thực hành này trình bày các khái niệm cơ bản của Django, tập trung vào URL routing, views, class-based views, và templates, giúp nắm được một số điều cốt lõi sau:
1. Django URLconfs
•	Hiểu vai trò của URLconfs trong việc định tuyến (routing).
•	Biết cách ánh xạ (map) một đường dẫn URL đến một view cụ thể.
•	Nhận ra đây là “cầu nối” giữa request của người dùng và logic xử lý trong view.
2. Django View functions
•	Nắm được cách xây dựng view function để xử lý request và trả về response.
•	Biết sử dụng context để truyền dữ liệu từ view sang template.
3. Class-based Views (CBV)
•	CBV như một cách tổ chức code rõ ràng, dễ tái sử dụng hơn so với function-based views.
•	Hiểu rằng CBV có sẵn nhiều generic view (như ListView, DetailView, …) giúp giảm lặp code.
•	CBV phù hợp khi xây dựng các ứng dụng lớn, có tính mở rộng cao.
4. Templates trong Django
•	Biết cách tách phần giao diện (HTML) ra khỏi logic xử lý.
•	Sử dụng template để hiển thị dữ liệu động 
•	Hiểu cơ chế kết hợp giữa context (từ view) và template để render nội dung cho người dùng.
