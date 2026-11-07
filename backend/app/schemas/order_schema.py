def serialize_order(order: dict) -> dict:
    """
    Chuyển đổi dictionary thô từ Supabase thành format chuẩn JSON cho API response.
    """
    if not order:
        return {}

    # Xử lý lấy tên khách hàng từ bảng join users (nếu có select kèm users)
    customer_info = order.get("users")
    customer_name = customer_info.get("full_name") if customer_info else None

    return {
        "id": order.get("id"),
        "customer_id": order.get("customer_id"),
        "customer_name": customer_name,
        # Ép kiểu Decimal/Numeric sang string để tránh lỗi serialize JSON của Flask
        "total_amount": str(order.get("total_amount")) if order.get("total_amount") is not None else "0.00",
        "status": order.get("status"),
        "note": order.get("note"),
        "created_at": order.get("created_at"), # Supabase thường trả về string ISO format sẵn
    }

def serialize_order_item(item: dict) -> dict:
    """Serialize chi tiết sản phẩm trong hóa đơn"""
    product_info = item.get("products")
    return {
        "id": item.get("id"),
        "product_id": item.get("product_id"),
        "product_name": product_info.get("name") if product_info else None,
        "quantity": item.get("quantity"),
        "unit_price": str(item.get("unit_price")),
    }