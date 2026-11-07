from app.database_connector import db 

class OrderService:
    @staticmethod
    def get_all_orders(filters=None):
        """
        Liệt kê toàn bộ đơn hàng, có hỗ trợ lọc linh hoạt theo status hoặc customer_id.
        filters: dict, ví dụ: {"status": "pending_approve", "customer_id": 1}
        """
        try:
            # response = db.table("invoices").select("*").execute()
            # print(response.data)
            query = db.table("invoices").select("*, users(full_name, email)")

            # Áp dụng bộ lọc nếu có
            if filters:
                if "status" in filters and filters["status"]:
                    query = query.eq("status", filters["status"])
                if "customer_id" in filters and filters["customer_id"]:
                    query = query.eq("customer_id", filters["customer_id"])

            response = query.order("created_at", desc=True).execute()
            
            return {
                "success": True,
                "data": response.data,
                "message": "Lấy danh sách đơn hàng thành công."
            }
        except Exception as e:
            return {
                "success": False,
                "data": [],
                "message": f"Lỗi khi lấy danh sách đơn hàng: {str(e)}"
            }

    @staticmethod
    def get_pending_orders():
        """
        Lấy danh sách các đơn đang chờ duyệt (pending_approve).
        Đây là danh sách chính mà AI Agent sẽ quét qua để thực hiện auto-approve hoặc review.
        """
        try:
            response = db.table("invoices") \
                .select("id, customer_id, total_amount, status, created_at, users(full_name, email)") \
                .eq("status", "pending_approve") \
                .order("created_at", desc=False) \
                .execute()

            return {
                "success": True,
                "data": response.data,
                "message": f"Tìm thấy {len(response.data)} đơn hàng đang chờ duyệt."
            }
        except Exception as e:
            return {
                "success": False,
                "data": [],
                "message": f"Lỗi khi lấy danh sách đơn chờ duyệt: {str(e)}"
            }

    @staticmethod
    def get_order_detail(order_id: int):
        """
        Xem chi tiết thông tin hóa đơn, thông tin khách hàng và danh sách sản phẩm bên trong đơn hàng đó.
        """
        try:
            # 1. Lấy thông tin chung của hóa đơn kèm thông tin user
            invoice_res = db.table("invoices") \
                .select("*, users(id, full_name, email, role)") \
                .eq("id", order_id) \
                .execute()

            if not invoice_res.data:
                return {
                    "success": False,
                    "data": None,
                    "message": f"Không tìm thấy đơn hàng với ID: {order_id}"
                }

            invoice_data = invoice_res.data[0]

            # 2. Lấy chi tiết các sản phẩm trong hóa đơn (invoice_items kết hợp bảng products)
            items_res = db.table("invoice_items") \
                .select("id, quantity, unit_price, products(id, name, price, stock_quantity)") \
                .eq("invoice_id", order_id) \
                .execute()

            # Gắn danh sách item vào kết quả trả về
            invoice_data["items"] = items_res.data

            return {
                "success": True,
                "data": invoice_data,
                "message": f"Lấy chi tiết đơn hàng #{order_id} thành công."
            }
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Lỗi khi truy vấn chi tiết đơn hàng: {str(e)}"
            }
        