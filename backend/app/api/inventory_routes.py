from flask import Blueprint, jsonify
# from app.repositories.product_repository import list_products

bp = Blueprint("inventory", __name__, url_prefix="/api/inventory")


@bp.get("")
def get_inventory():
    return jsonify(data=[])
