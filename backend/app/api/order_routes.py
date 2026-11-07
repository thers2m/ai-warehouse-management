from flask import Blueprint, jsonify, request
from app.repositories.order_repository import list_orders
from app.schemas.order_schema import serialize_order

bp = Blueprint("orders", __name__, url_prefix="/api/orders")
VALID_STATUSES = {"pending_approve", "approved", "rejected", "requires_human_review"}


@bp.get("")
def get_orders():
    status = request.args.get("status")
    if status and status not in VALID_STATUSES:
        return jsonify(error="Invalid status"), 400
    return jsonify(data=[serialize_order(o) for o in list_orders(status)])
