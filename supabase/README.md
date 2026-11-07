# Supabase

Bốn bảng nghiệp vụ là `public.users`, `public.products`, `public.invoices`, `public.invoice_items`.

Nếu đã tạo chúng trên Supabase, **không chạy lại** script create-table.

Dùng Supabase CLI để quản lý migrations khi cần. Backend kết nối PostgreSQL qua SQLAlchemy, không tự tạo tables khi chạy Flask.
