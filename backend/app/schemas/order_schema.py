def serialize_order(order):
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "customer_name": order.customer.full_name if order.customer else None,
        "total_amount": str(order.total_amount),
        "status": order.status,
        "note": order.note,
        "created_at": order.created_at.isoformat() if order.created_at else None,
    }
