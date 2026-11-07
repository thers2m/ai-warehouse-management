# API hiện đã có

- `GET /api/health` - kiểm tra Flask
- `GET /api/products` - danh sách sản phẩm
- `GET /api/orders?status=pending_approve` - danh sách đơn hàng / lọc trạng thái
- `GET /api/inventory` - tồn kho từ products
- `POST /api/agent/chat` - placeholder 501, chưa chạy AI

Các endpoint ghi (tạo/duyệt/từ chối/hủy) sẽ bổ sung sau khi có auth, transaction và kiểm tra tồn kho.
