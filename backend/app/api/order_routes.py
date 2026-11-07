from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService
from app.schemas.order_schema import serialize_order, serialize_order_item

order_bp = Blueprint("orders", __name__, url_prefix="/api/orders")
VALID_STATUSES = {"pending_approve", "approved", "rejected", "requires_human_review"}


@order_bp.route('', methods=['GET'])
def get_all_orders():
    """
    API 1: Liệt kê toàn bộ đơn hàng hoặc lọc theo status/customer_id
    Endpoint: GET /api/orders?status=pending_approve&customer_id=1
    """
    status = request.args.get('status')
    customer_id = request.args.get('customer_id')

    filters = {}
    if status:
        if status not in VALID_STATUSES:
            return jsonify({
                "success": False,
                "message": f"Status không hợp lệ. Các status cho phép: {list(VALID_STATUSES)}"
            }), 400
        filters['status'] = status

    if customer_id:
        try:
            filters['customer_id'] = int(customer_id)
        except ValueError:
            return jsonify({
                "success": False,
                "message": "customer_id phải là số nguyên hợp lệ."
            }), 400

    # Gọi service lấy dữ liệu từ DB
    result = OrderService.get_all_orders(filters)

    if result["success"]:
        # Sử dụng schema để serialize danh sách đơn hàng
        serialized_data = [serialize_order(order) for order in result["data"]]
        return jsonify({
            "success": True,
            "data": serialized_data,
            "message": result["message"]
        }), 200
    else:
        return jsonify(result), 500


@order_bp.route('/pending', methods=['GET'])
def get_pending_orders():
    """
    API 2: Lấy danh sách các đơn đang chờ duyệt (pending_approve)
    Endpoint: GET /api/orders/pending
    (Danh sách mà Agent hoặc Nhân viên sẽ quét qua)
    """
    result = OrderService.get_pending_orders()

    if result["success"]:
        # Serialize danh sách đơn chờ duyệt
        serialized_data = [serialize_order(order) for order in result["data"]]
        return jsonify({
            "success": True,
            "data": serialized_data,
            "message": result["message"]
        }), 200
    else:
        return jsonify(result), 500


@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order_detail(order_id: int):
    """
    API 3: Xem chi tiết sản phẩm và tổng tiền của 1 đơn hàng cụ thể
    Endpoint: GET /api/orders/1
    """
    result = OrderService.get_order_detail(order_id)

    if result["success"]:
        order_raw = result["data"]
        
        # Serialize thông tin chung của hóa đơn
        serialized_invoice = serialize_order(order_raw)
        
        # Serialize danh sách các sản phẩm (items) bên trong đơn hàng
        raw_items = order_raw.get("items", [])
        serialized_invoice["items"] = [serialize_order_item(item) for item in raw_items]

        return jsonify({
            "success": True,
            "data": serialized_invoice,
            "message": result["message"]
        }), 200
    else:
        status_code = 404 if "Không tìm thấy" in result["message"] else 500
        return jsonify(result), status_code